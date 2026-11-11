import { readSalaForm, updateSalaCard, updateSalaEmptyState } from "./dados.js";

export function initCreateSala(showToast) {
    var form = document.getElementById("cadastrar-sala-form");
    var list = document.querySelector("[data-sala-list]");
    var template = document.getElementById("sala-card-template");
    if (!form || !list || !template) return;

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        form.elements.namedItem("nome").value = form.elements.namedItem("nome").value.trim();
        if (!form.reportValidity()) return;

        var card = template.content.querySelector("[data-sala-card]").cloneNode(true);
        updateSalaCard(card, readSalaForm(form));
        list.insertBefore(card, list.querySelector("[data-sala-empty]"));
        updateSalaEmptyState(list);
        form.reset();
        form.elements.namedItem("nome").focus();
        showToast("Sala adicionada à prévia. Os dados não foram salvos no banco.");
    });
}
