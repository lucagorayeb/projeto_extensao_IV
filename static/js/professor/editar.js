export function initEditProfessor() {
    var modalEl = document.getElementById("edit-professor-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var submitBtn = form.querySelector('[type="submit"]');
    var errorEl = form.querySelector("[data-edit-error]");
    var trigger = null;
    var pending = false;

    document.querySelectorAll('[data-action="edit"][data-entity="professor"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            form.reset();
            errorEl.hidden = true;
            errorEl.textContent = "";
            form.elements.namedItem("id").value = btn.getAttribute("data-id");
            form.elements.namedItem("nome").value = btn.getAttribute("data-edit-name") || "";
            form.elements.namedItem("cpf").value = btn.getAttribute("data-edit-cpf") || "";
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
        if (pending || !form.reportValidity()) return;

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
