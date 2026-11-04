import { useState } from "react"
import { Building2 } from "lucide-react"
import { toast } from "sonner"
import { EMPTY_SALA_FORM, SalaForm, salaToForm } from "@/components/cadastro/sala-form"
import { SalaItem } from "@/components/cadastro/sala-item"
import { EmptyState } from "@/components/shared/empty-state"
import { Panel } from "@/components/shared/panel"
import { useSchedule } from "@/context/schedule-context"
import type { Sala } from "@/types"

export function SalasTab() {
  const { salas, addSala, updateSala, removeSala, isBackendConnected } = useSchedule()
  const [editing, setEditing] = useState<Sala | null>(null)
  const [formKey, setFormKey] = useState(0) // remonta o formulário ao salvar/cancelar/editar

  const reset = () => {
    setEditing(null)
    setFormKey((k) => k + 1)
  }

  return (
    <div className="grid gap-5 lg:grid-cols-5">
      <Panel className="h-fit lg:sticky lg:top-5 lg:col-span-2">
        <div className="mb-4 flex items-center justify-between gap-2">
          <h2 className="text-sm font-semibold">
            {editing ? "Editar sala" : "Nova sala ou laboratório"}
          </h2>
          <span
            className={`inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[11px] font-medium ${
              isBackendConnected
                ? "bg-emerald-50 text-emerald-700 dark:bg-emerald-950/50 dark:text-emerald-300"
                : "bg-amber-50 text-amber-700 dark:bg-amber-950/50 dark:text-amber-300"
            }`}
          >
            <span
              className={`size-1.5 rounded-full ${
                isBackendConnected ? "bg-emerald-500 animate-pulse" : "bg-amber-500"
              }`}
            />
            {isBackendConnected ? "API Conectada" : "Modo Local"}
          </span>
        </div>
        <SalaForm
          key={formKey}
          initial={editing ? salaToForm(editing) : EMPTY_SALA_FORM}
          editing={!!editing}
          onCancel={reset}
          onSubmit={async (input) => {
            if (editing) {
              await updateSala(editing.id, input)
              toast.success("Sala atualizada.")
            } else {
              await addSala(input)
              toast.success("Sala cadastrada.")
            }
            reset()
          }}
        />
      </Panel>

      <div className="flex flex-col gap-2.5 lg:col-span-3">
        {salas.length === 0 ? (
          <Panel>
            <EmptyState
              icon={Building2}
              title="Nenhuma sala cadastrada"
              description="Cadastre a primeira sala ou laboratório."
            />
          </Panel>
        ) : (
          salas.map((s) => (
            <SalaItem
              key={s.id}
              sala={s}
              onEdit={() => {
                setEditing(s)
                setFormKey((k) => k + 1)
              }}
              onDelete={() => {
                const res = removeSala(s.id)
                if (!res.ok) return toast.error(res.message)
                toast.success("Sala removida.")
                if (editing?.id === s.id) reset()
              }}
            />
          ))
        )}
      </div>
    </div>
  )
}
