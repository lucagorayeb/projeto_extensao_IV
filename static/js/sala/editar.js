import { salaFields, readSalaForm, updateSalaCard } from "./dados.js";

export function initEditSala(showToast) {
    var modalEl = document.getElementById("edit-sala-modal");
    var list = document.querySelector("[data-sala-list]");
    if (!modalEl || !list || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var trigger = null;
    var card = null;

    list.addEventListener("click", function (event) {
        var btn = event.target.closest('[data-action="edit"][data-entity="sala"]');
        if (!btn || btn.disabled || trigger) return;
        trigger = btn;
        card = btn.closest("[data-sala-card]");
        form.reset();
        salaFields.forEach(function (field) {
            var input = form.elements.namedItem(field);
            var value = card.dataset[field] || "";
            if (input.tagName === "SELECT" && !Array.from(input.options).some(function (option) { return option.value === value; })) {
                input.add(new Option(value, value));
            }
            input.value = value;
        });
        modal.show();
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        form.elements.namedItem("nome").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
        card = null;
    });

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        form.elements.namedItem("nome").value = form.elements.namedItem("nome").value.trim();
        if (!card || !form.reportValidity()) return;
        updateSalaCard(card, readSalaForm(form));
        modal.hide();
        showToast("Sala atualizada na prévia. Os dados não foram salvos no banco.");
    });
}
