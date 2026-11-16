import { responseErrorMessage } from "../shared/error-modal.js";

export function initEditTurma() {
    var modalEl = document.getElementById("edit-turma-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var submitBtn = form.querySelector('[type="submit"]');
    var errorEl = form.querySelector("[data-edit-error]");
    var trigger = null;
    var pending = false;

    document.querySelectorAll('[data-action="edit"][data-entity="turma"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            form.reset();
            errorEl.hidden = true;
            errorEl.textContent = "";
            form.elements.namedItem("id").value = btn.getAttribute("data-id");
            ["fk_disciplina", "fk_professor", "fk_sala", "fk_dia_semana", "horario_inicio", "horario_fim"].forEach(function (field) {
                var value = btn.getAttribute("data-edit-" + field.replaceAll("_", "-")) || "";
                if (field.startsWith("horario_")) {
                    value = value.split(":").map(function (part) { return part.padStart(2, "0"); }).join(":");
                }
                form.elements.namedItem(field).value = value;
            });
            modal.show();
        });
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        form.elements.namedItem("fk_disciplina").focus();
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
        if (pending || !trigger || !form.reportValidity()) return;
        pending = true;
        submitBtn.disabled = true;
        submitBtn.textContent = "Salvando…";
        errorEl.hidden = true;
        form.setAttribute("aria-busy", "true");
        try {
            var response = await fetch(form.action, {
                method: "PUT",
                body: new FormData(form),
                headers: { Accept: "application/json" },
            });
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
