export function initViewDisciplina() {
    var modalEl = document.getElementById("view-disciplina-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;
    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var trigger = null;

    document.querySelectorAll('[data-action="view"][data-entity="disciplina"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            var data = btn.closest("[data-disciplina-card]").dataset;
            modalEl.querySelector("[data-disciplina-nome]").textContent = data.nome || "Não informado";
            modalEl.querySelector("[data-disciplina-formato]").textContent = data.formato || "Não informado";
            modalEl.querySelector("[data-disciplina-carga-horaria]").textContent = data.cargaHoraria || "Não informado";
            modalEl.querySelector("[data-disciplina-pratica]").textContent = data.pratica === "1" ? "Sim" : "Não";
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
