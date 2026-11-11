export var salaFields = ["nome", "tipo", "capacidade"];

export function readSalaForm(form) {
    var data = {};
    salaFields.forEach(function (field) {
        data[field] = form.elements.namedItem(field).value.trim();
    });
    return data;
}

export function renderSala(element, data) {
    salaFields.forEach(function (field) {
        element.querySelector("[data-sala-" + field + "]").textContent = data[field] || "Não informada";
    });
}

export function updateSalaCard(card, data) {
    salaFields.forEach(function (field) {
        card.dataset[field] = data[field];
    });
    renderSala(card, data);
    card.querySelector('[role="group"]').setAttribute("aria-label", "Ações de " + data.nome);
    card.querySelector('[data-action="view"]').setAttribute("aria-label", "Visualizar dados de " + data.nome);
    card.querySelector('[data-action="edit"]').setAttribute("aria-label", "Editar " + data.nome);
    card.querySelector('[data-action="delete"]').setAttribute("aria-label", "Excluir " + data.nome);
}

export function updateSalaEmptyState(list) {
    list.querySelector("[data-sala-empty]").hidden = !!list.querySelector("[data-sala-card]");
}
