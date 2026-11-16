export function initViewTurma() {
    var modalEl = document.getElementById("view-turma-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var trigger = null;

    document.querySelectorAll('[data-action="view"][data-entity="turma"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            ["fk_disciplina_nome", "fk_professor_nome", "fk_sala_nome", "fk_dia_semana_nome", "horario_inicio", "horario_fim", "carga_horaria"].forEach(function (field) {
                var attribute = field.replaceAll("_", "-");
                modalEl.querySelector("[data-turma-" + attribute + "]").textContent = btn.getAttribute("data-view-" + attribute) || "Não informado";
            });
            modal.show();
        });
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-view-close]").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
    });
}
