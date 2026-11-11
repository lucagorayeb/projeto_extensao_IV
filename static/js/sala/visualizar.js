import { renderSala } from "./dados.js";

export function initViewSala() {
    var modalEl = document.getElementById("view-sala-modal");
    var list = document.querySelector("[data-sala-list]");
    if (!modalEl || !list || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var trigger = null;

    list.addEventListener("click", function (event) {
        var btn = event.target.closest('[data-action="view"][data-entity="sala"]');
        if (!btn || btn.disabled || trigger) return;
        trigger = btn;
        renderSala(modalEl, btn.closest("[data-sala-card]").dataset);
        modal.show();
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-view-close]").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
    });
}
