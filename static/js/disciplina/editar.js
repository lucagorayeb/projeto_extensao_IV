import { responseErrorMessage } from "../shared/error-modal.js";

export function initEditDisciplina() {
    var modalEl = document.getElementById("edit-disciplina-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;
    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var submitBtn = form.querySelector('[type="submit"]');
    var errorEl = form.querySelector("[data-edit-error]");
    var trigger = null;
    var pending = false;

    document.querySelectorAll('[data-action="edit"][data-entity="disciplina"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            var data = btn.closest("[data-disciplina-card]").dataset;
            form.reset();
            form.action = btn.getAttribute("data-edit-url");
            form.elements.namedItem("nome").value = data.nome;
            form.elements.namedItem("fk_formato").value = data.formatoId;
            form.elements.namedItem("carga_horaria").value = data.cargaHoraria;
            form.elements.namedItem("pratica").value = data.pratica;
            errorEl.hidden = true;
            errorEl.textContent = "";
            modal.show();
        });
    });
    modalEl.addEventListener("shown.bs.modal", function () {
        form.elements.namedItem("nome").focus();
    });
    modalEl.addEventListener("hide.bs.modal", function (event) {
        if (pending) event.preventDefault();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
    });
    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        form.elements.namedItem("nome").value = form.elements.namedItem("nome").value.trim();
        if (pending || !trigger || !form.reportValidity()) return;
        pending = true;
        submitBtn.disabled = true;
        submitBtn.textContent = "Salvando…";
        errorEl.hidden = true;
        form.setAttribute("aria-busy", "true");
        try {
            var response = await fetch(form.action, { method: "PUT", body: new FormData(form), headers: { Accept: "application/json" } });
            if (!response.ok) {
                errorEl.textContent = await responseErrorMessage(response);
                errorEl.hidden = false;
                return;
            }
            window.location.reload();
        } catch {
            errorEl.textContent = "Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.";
            errorEl.hidden = false;
        } finally {
            pending = false;
            submitBtn.disabled = false;
            submitBtn.textContent = "Salvar alterações";
            form.removeAttribute("aria-busy");
        }
    });
}
