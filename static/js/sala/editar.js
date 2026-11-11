export function initEditSala(showToast) {
    var modalEl = document.getElementById("edit-sala-modal");
    var list = document.querySelector("[data-sala-list]");
    if (!modalEl || !list || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var submitBtn = form.querySelector('[type="submit"]');
    var errorEl = form.querySelector("[data-edit-error]");
    var pending = false;
    var trigger = null;
    var card = null;

    list.addEventListener("click", function (event) {
        var btn = event.target.closest('[data-action="edit"][data-entity="sala"]');
        if (!btn || btn.disabled || trigger) return;
        trigger = btn;
        card = btn.closest("[data-sala-card]");
        form.reset();
        errorEl.hidden = true;
        errorEl.textContent = "";
        form.elements.namedItem("id").value = card.dataset.id;
        form.elements.namedItem("nome").value = card.dataset.nome;
        form.elements.namedItem("fk_tipo_sala").value = card.dataset.tipoId;
        form.elements.namedItem("limite_alunos").value = card.dataset.capacidade;
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
    modalEl.addEventListener("hide.bs.modal", function (event) {
        if (pending) event.preventDefault();
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        form.elements.namedItem("nome").value = form.elements.namedItem("nome").value.trim();
        if (pending || !card || !form.reportValidity()) return;
        pending = true;
        submitBtn.disabled = true;
        submitBtn.textContent = "Salvando…";
        errorEl.hidden = true;
        form.setAttribute("aria-busy", "true");
        try {
            var response = await fetch(form.action, {
                method: "PUT",
                body: new FormData(form),
            });
            if (!response.ok) throw new Error("HTTP " + response.status);
            window.location.reload();
        } catch (error) {
            errorEl.textContent = "Não foi possível salvar as alterações. Verifique os dados e tente novamente.";
            errorEl.hidden = false;
        } finally {
            pending = false;
            submitBtn.disabled = false;
            submitBtn.textContent = "Salvar alterações";
            form.removeAttribute("aria-busy");
        }
    });
}
