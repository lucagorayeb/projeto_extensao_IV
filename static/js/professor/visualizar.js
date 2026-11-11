export function initViewProfessor() {
    var modalEl = document.getElementById("view-professor-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var trigger = null;

    document.querySelectorAll('[data-action="view"][data-entity="professor"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            modalEl.querySelector("[data-professor-name]").textContent = btn.getAttribute("data-view-name") || "Não informado";
            modalEl.querySelector("[data-professor-cpf]").textContent = btn.getAttribute("data-view-cpf") || "Não informado";
            modalEl.querySelector("[data-professor-specialty]").textContent = btn.getAttribute("data-view-specialty") || "Nenhuma especialidade vinculada";
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
