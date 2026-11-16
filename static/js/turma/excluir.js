import { responseErrorMessage } from "../shared/error-modal.js";

export function initDeleteTurma() {
    var modalEl = document.getElementById("delete-turma-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var confirmBtn = modalEl.querySelector("[data-confirm-delete]");
    var errorEl = modalEl.querySelector("[data-delete-error]");
    var trigger = null;
    var pending = false;

    document.querySelectorAll('[data-action="delete"][data-entity="turma"][data-turma-delete-url]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            var title = btn.closest(".panel").querySelector(".list-item-title");
            modalEl.querySelector("[data-delete-name]").textContent = title.textContent.trim();
            errorEl.hidden = true;
            errorEl.textContent = "";
            modal.show();
        });
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-delete-cancel]").focus();
    });
    modalEl.addEventListener("hide.bs.modal", function (event) {
        if (pending) event.preventDefault();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
    });

    confirmBtn.addEventListener("click", async function () {
        if (pending || !trigger) return;
        pending = true;
        confirmBtn.disabled = true;
        var originalLabel = confirmBtn.innerHTML;
        confirmBtn.textContent = "Excluindo…";
        errorEl.hidden = true;
        modalEl.setAttribute("aria-busy", "true");

        try {
            var response = await fetch(trigger.getAttribute("data-turma-delete-url"), {
                method: "DELETE",
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
            confirmBtn.disabled = false;
            confirmBtn.innerHTML = originalLabel;
            modalEl.removeAttribute("aria-busy");
        }
    });
}
