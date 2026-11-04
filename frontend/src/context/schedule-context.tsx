
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react"
import { detectConflicts } from "@/lib/schedule"
import {
  fetchSalasFromBackend,
  fetchTiposSala,
  createSalaInBackend,
  updateSalaInBackend,
  deleteSalaInBackend,
  type BackendTipoSala,
} from "@/services/sala"
import type {
  Professor,
  ProfessorInput,
  Sala,
  SalaInput,
  Turma,
  TurmaInput,
} from "@/types"

export type ActionResult = { ok: true } | { ok: false; message: string }

interface ScheduleContextValue {
  salas: Sala[]
  professores: Professor[]
  turmas: Turma[]
  conflitos: Set<string>
  isBackendConnected: boolean
  getSala: (id?: string | null) => Sala | undefined
  getProfessor: (id?: string | null) => Professor | undefined
  addSala: (input: SalaInput) => Promise<void> | void
  updateSala: (id: string, input: SalaInput) => Promise<void> | void
  removeSala: (id: string) => ActionResult
  addProfessor: (input: ProfessorInput) => void
  updateProfessor: (id: string, input: ProfessorInput) => void
  removeProfessor: (id: string) => ActionResult
  addTurma: (input: TurmaInput) => void
  updateTurma: (id: string, input: TurmaInput) => void
  removeTurma: (id: string) => void
  refreshSalas: () => Promise<void>
}

const ScheduleContext = createContext<ScheduleContextValue | null>(null)

const STORAGE_KEY = "engetec-schedule-v1"

const newId = (prefix: string) =>
  `${prefix}_${crypto.randomUUID().slice(0, 8)}`

interface SavedData {
  salas: Sala[]
  professores: Professor[]
  turmas: Turma[]
}

const EMPTY_DATA: SavedData = {
  salas: [],
  professores: [],
  turmas: [],
}

function loadData(): SavedData {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)

    if (!saved) return EMPTY_DATA

    const data = JSON.parse(saved) as Partial<SavedData>

    return {
      salas: Array.isArray(data.salas) ? data.salas : [],
      professores: Array.isArray(data.professores)
        ? data.professores
        : [],
      turmas: Array.isArray(data.turmas) ? data.turmas : [],
    }
  } catch {
    return EMPTY_DATA
  }
}

interface ProviderProps {
  children: ReactNode
  initialSalas?: Sala[]
  initialProfessores?: Professor[]
  initialTurmas?: Turma[]
}

export function ScheduleProvider({
  children,
  initialSalas,
  initialProfessores,
  initialTurmas,
}: ProviderProps) {
  const [initialData] = useState<SavedData>(() => {
    const saved = loadData()

    const hasSavedData = localStorage.getItem(STORAGE_KEY) !== null

    if (hasSavedData) return saved

    return {
      salas: initialSalas ?? [],
      professores: initialProfessores ?? [],
      turmas: initialTurmas ?? [],
    }
  })

  const [salas, setSalas] = useState<Sala[]>(initialData.salas)
  const [professores, setProfessores] = useState<Professor[]>(
    initialData.professores,
  )
  const [turmas, setTurmas] = useState<Turma[]>(initialData.turmas)
  const [tiposSala, setTiposSala] = useState<BackendTipoSala[]>([])
  const [isBackendConnected, setIsBackendConnected] = useState<boolean>(false)

  const refreshSalas = useCallback(async () => {
    const backendSalas = await fetchSalasFromBackend()
    if (backendSalas !== null) {
      setIsBackendConnected(true)
      if (backendSalas.length > 0) {
        setSalas(backendSalas)
      }
    } else {
      setIsBackendConnected(false)
    }
  }, [])

  // Sincronização inicial com o backend FastAPI
  useEffect(() => {
    let isMounted = true

    async function sync() {
      const [backendTipos, backendSalas] = await Promise.all([
        fetchTiposSala(),
        fetchSalasFromBackend(),
      ])

      if (!isMounted) return

      if (backendTipos && backendTipos.length > 0) {
        setTiposSala(backendTipos)
      }

      if (backendSalas !== null) {
        setIsBackendConnected(true)
        if (backendSalas.length > 0) {
          setSalas(backendSalas)
        }
      } else {
        setIsBackendConnected(false)
      }
    }

    sync()

    return () => {
      isMounted = false
    }
  }, [])

  useEffect(() => {
    try {
      const data: SavedData = { salas, professores, turmas }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data))
    } catch (error) {
      console.error("Não foi possível salvar os dados do Painel Engetec:", error)
    }
  }, [salas, professores, turmas])

  const conflitos = useMemo(
    () => detectConflicts(turmas, salas),
    [turmas, salas],
  )

  const getSala = useCallback(
    (id?: string | null) => salas.find((s) => s.id === id),
    [salas],
  )

  const getProfessor = useCallback(
    (id?: string | null) => professores.find((p) => p.id === id),
    [professores],
  )

  const addSala = useCallback(
    async (input: SalaInput) => {
      // 1. Atualização otimista imediata na UI
      const tempId = newId("s")
      setSalas((prev) => [{ id: tempId, ...input }, ...prev])

      // 2. Envia para o backend FastAPI
      const res = await createSalaInBackend(input, tiposSala)
      if (res.ok) {
        // Recarrega do backend para sincronizar os IDs reais do banco de dados
        await refreshSalas()
      }
    },
    [tiposSala, refreshSalas],
  )

  const updateSala = useCallback(
    async (id: string, input: SalaInput) => {
      setSalas((prev) =>
        prev.map((s) => (s.id === id ? { ...s, ...input } : s)),
      )
      await updateSalaInBackend(id, input, tiposSala)
    },
    [tiposSala],
  )

  const removeSala = useCallback(
    (id: string): ActionResult => {
      const sala = salas.find((s) => s.id === id)

      if (turmas.some((t) => t.salaId === id)) {
        return {
          ok: false,
          message: `Não é possível excluir: ${sala?.nome ?? "a sala"} está vinculada a turmas cadastradas.`,
        }
      }

      setSalas((prev) => prev.filter((s) => s.id !== id))
      deleteSalaInBackend(id).catch((err) =>
        console.warn("Erro ao excluir sala no backend:", err),
      )
      return { ok: true }
    },
    [salas, turmas],
  )

  const addProfessor = useCallback((input: ProfessorInput) => {
    setProfessores((prev) => [{ id: newId("p"), ...input }, ...prev])
  }, [])

  const updateProfessor = useCallback(
    (id: string, input: ProfessorInput) => {
      setProfessores((prev) =>
        prev.map((p) => (p.id === id ? { ...p, ...input } : p)),
      )
    },
    [],
  )

  const removeProfessor = useCallback(
    (id: string): ActionResult => {
      const professor = professores.find((p) => p.id === id)

      if (turmas.some((t) => t.professorId === id)) {
        return {
          ok: false,
          message: `Não é possível excluir: ${professor?.nome ?? "o professor"} está vinculado a turmas cadastradas.`,
        }
      }

      setProfessores((prev) => prev.filter((p) => p.id !== id))
      return { ok: true }
    },
    [professores, turmas],
  )

  const addTurma = useCallback((input: TurmaInput) => {
    setTurmas((prev) => [{ id: newId("t"), ...input }, ...prev])
  }, [])

  const updateTurma = useCallback((id: string, input: TurmaInput) => {
    setTurmas((prev) =>
      prev.map((t) => (t.id === id ? { ...t, ...input } : t)),
    )
  }, [])

  const removeTurma = useCallback((id: string) => {
    setTurmas((prev) => prev.filter((t) => t.id !== id))
  }, [])

  const value = useMemo<ScheduleContextValue>(
    () => ({
      salas,
      professores,
      turmas,
      conflitos,
      isBackendConnected,
      getSala,
      getProfessor,
      addSala,
      updateSala,
      removeSala,
      addProfessor,
      updateProfessor,
      removeProfessor,
      addTurma,
      updateTurma,
      removeTurma,
      refreshSalas,
    }),
    [
      salas,
      professores,
      turmas,
      conflitos,
      isBackendConnected,
      getSala,
      getProfessor,
      addSala,
      updateSala,
      removeSala,
      addProfessor,
      updateProfessor,
      removeProfessor,
      addTurma,
      updateTurma,
      removeTurma,
      refreshSalas,
    ],
  )

  return (
    <ScheduleContext.Provider value={value}>
      {children}
    </ScheduleContext.Provider>
  )
}

export function useSchedule() {
  const ctx = useContext(ScheduleContext)

  if (!ctx) {
    throw new Error("useSchedule deve ser usado dentro de <ScheduleProvider>")
  }

  return ctx
}
