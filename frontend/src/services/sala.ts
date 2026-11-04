import { API_URL } from "@/config/api"
import type { Sala, SalaInput, TipoSala } from "@/types"

export interface BackendSala {
  id: number
  nome_sala: string
  quantidade_alunos: number
  tipo_sala_id: number
  tipo_sala: string
}

export interface BackendSalaDTO {
  nome: string
  limite_alunos: number
  fk_tipo_sala: number
}

export interface BackendTipoSala {
  id: number
  tipo_sala: string
}

/**
 * Converte o tipo de sala textual do frontend para o id numérico de chave estrangeira do backend.
 */
export function mapTipoSalaToId(tipo: TipoSala, tiposSalaBackend?: BackendTipoSala[]): number {
  if (tiposSalaBackend && tiposSalaBackend.length > 0) {
    const found = tiposSalaBackend.find((t) => {
      const lower = t.tipo_sala.toLowerCase()
      if (tipo === "laboratorio" && lower.includes("lab")) return true
      if (tipo === "online" && (lower.includes("virtual") || lower.includes("online") || lower.includes("ava"))) return true
      if (tipo === "sala" && (lower.includes("sala") || lower.includes("aula"))) return true
      return false
    })
    if (found) return found.id
  }

  // Mapeamento padrão de fallback
  switch (tipo) {
    case "laboratorio":
      return 2
    case "online":
      return 3
    case "sala":
    default:
      return 1
  }
}

/**
 * Converte o ID e nome retornado pelo backend para o tipo de sala do frontend.
 */
export function mapIdToTipoSala(id: number, nomeTipo?: string): TipoSala {
  if (nomeTipo) {
    const lower = nomeTipo.toLowerCase()
    if (lower.includes("lab")) return "laboratorio"
    if (lower.includes("virtual") || lower.includes("online") || lower.includes("ava")) return "online"
    if (lower.includes("sala") || lower.includes("aula")) return "sala"
  }
  if (id === 2) return "laboratorio"
  if (id === 3) return "online"
  return "sala"
}

/**
 * Converte a entidade retornada pela API do FastAPI no formato da interface Sala do React.
 */
export function backendSalaToFrontend(b: BackendSala): Sala {
  return {
    id: String(b.id),
    nome: b.nome_sala,
    capacidade: Number(b.quantidade_alunos) || 0,
    tipo: mapIdToTipoSala(b.tipo_sala_id, b.tipo_sala),
    predio: "Central", // Padrão pois o banco atual não possui campo prédio
    andar: "Térreo",   // Padrão pois o banco atual não possui campo andar
  }
}

/**
 * Converte o formulário de cadastro do frontend no payload esperado pelo SalaDTO do FastAPI.
 */
export function frontendInputToBackend(input: SalaInput, tiposSalaBackend?: BackendTipoSala[]): BackendSalaDTO {
  return {
    nome: input.nome,
    limite_alunos: Number(input.capacidade) || 0,
    fk_tipo_sala: mapTipoSalaToId(input.tipo, tiposSalaBackend),
  }
}

/**
 * Busca a lista de tipos de sala disponíveis no backend.
 */
export async function fetchTiposSala(): Promise<BackendTipoSala[]> {
  try {
    const res = await fetch(`${API_URL}/tipo-sala/`)
    if (!res.ok) return []
    const data = await res.json()
    return Array.isArray(data) ? data : []
  } catch {
    return []
  }
}

/**
 * Busca todas as salas cadastradas na API FastAPI.
 * Retorna `null` caso a API esteja offline para que o frontend utilize fallback local.
 */
export async function fetchSalasFromBackend(): Promise<Sala[] | null> {
  try {
    const res = await fetch(`${API_URL}/sala/`)
    if (!res.ok) {
      // Se o backend responder 500 (quando tabela vazia) ou 404, retorna lista vazia
      if (res.status === 404 || res.status === 500) {
        return []
      }
      return null
    }

    const data = await res.json()
    if (!Array.isArray(data)) return []

    return data.map(backendSalaToFrontend)
  } catch (error) {
    console.warn("API de salas não acessível no momento:", error)
    return null
  }
}

/**
 * Envia uma nova sala para a API FastAPI (POST /sala/).
 */
export async function createSalaInBackend(
  input: SalaInput,
  tiposSalaBackend?: BackendTipoSala[]
): Promise<{ ok: boolean; error?: string }> {
  try {
    const payload = frontendInputToBackend(input, tiposSalaBackend)
    const res = await fetch(`${API_URL}/sala/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })

    if (!res.ok) {
      return { ok: false, error: `Erro ${res.status}: falha ao cadastrar no backend.` }
    }

    return { ok: true }
  } catch {
    return { ok: false, error: "Erro de conexão ao cadastrar sala no backend." }
  }
}

/**
 * Atualiza uma sala existente na API FastAPI (PUT /sala/{id}).
 */
export async function updateSalaInBackend(
  id: string,
  input: SalaInput,
  tiposSalaBackend?: BackendTipoSala[]
): Promise<{ ok: boolean; error?: string }> {
  const numericId = parseInt(id, 10)
  if (isNaN(numericId)) {
    // Sala local/mock sem ID numérico no MySQL
    return { ok: true }
  }

  try {
    const payload = frontendInputToBackend(input, tiposSalaBackend)
    const res = await fetch(`${API_URL}/sala/${numericId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })

    if (!res.ok) {
      return { ok: false, error: `Erro ${res.status}: falha ao atualizar no backend.` }
    }

    return { ok: true }
  } catch {
    return { ok: false, error: "Erro de conexão ao atualizar sala no backend." }
  }
}

/**
 * Remove uma sala existente na API FastAPI (DELETE /sala/{id}).
 */
export async function deleteSalaInBackend(id: string): Promise<{ ok: boolean; error?: string }> {
  const numericId = parseInt(id, 10)
  if (isNaN(numericId)) {
    // Sala local/mock sem ID numérico no MySQL
    return { ok: true }
  }

  try {
    const res = await fetch(`${API_URL}/sala/${numericId}`, {
      method: "DELETE",
    })

    if (!res.ok) {
      return { ok: false, error: `Erro ${res.status}: falha ao excluir no backend.` }
    }

    return { ok: true }
  } catch {
    return { ok: false, error: "Erro de conexão ao excluir sala no backend." }
  }
}
