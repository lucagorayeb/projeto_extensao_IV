import { responseErrorMessage, showErrorModal } from "./error-modal.js";

export function initFormErrors() {
    document.querySelectorAll("form[data-error-modal]").forEach(function (form) {
        let pending = false;

        form.addEventListener("submit", async function (event) {
            event.preventDefault();
            if (pending || !form.reportValidity()) return;

            const data = new FormData(form);
            if (event.submitter && event.submitter.name) data.append(event.submitter.name, event.submitter.value);
            const trigger = document.activeElement;
            const buttons = Array.from(form.querySelectorAll('[type="submit"]'));
            const disabledStates = buttons.map(function (button) { return button.disabled; });
            pending = true;
            buttons.forEach(function (button) { button.disabled = true; });
            form.setAttribute("aria-busy", "true");

            let errorMessage = null;
            let errorTitle = "Não foi possível concluir";
            try {
                const response = await fetch(form.action, {
                    method: form.method.toUpperCase(),
                    body: data,
                    headers: { Accept: "application/json" },
                });
                if (!response.ok) {
                    errorMessage = await responseErrorMessage(response);
                    if (response.status === 409) errorTitle = "Conflito no cadastro";
                } else if (response.redirected) {
                    window.location.assign(response.url);
                } else {
                    window.location.reload();
                }
            } catch {
                errorMessage = "Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.";
            } finally {
                pending = false;
                buttons.forEach(function (button, index) { button.disabled = disabledStates[index]; });
                form.removeAttribute("aria-busy");
            }

            if (errorMessage) await showErrorModal(errorMessage, { title: errorTitle, trigger });
        });
    });
}
