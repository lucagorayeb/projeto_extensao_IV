export function initAddSpecialty() {
    var modalEl = document.getElementById("add-specialty-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var form = modalEl.querySelector("form");
    var select = form.elements.namedItem("fk_especialidade");
    var submitBtn = form.querySelector('[type="submit"]');
    var errorEl = form.querySelector("[data-specialty-error]");
    var trigger = null;
    var pending = false;

    document.querySelectorAll('[data-action="add-specialty"][data-entity="professor"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            form.reset();
            errorEl.hidden = true;
            errorEl.textContent = "";
            form.elements.namedItem("fk_professor").value = btn.getAttribute("data-id");
            var title = btn.closest(".panel").querySelector(".list-item-title");
            modalEl.querySelector("[data-specialty-professor]").textContent = title.textContent.trim();
            modal.show();
        });
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        if (!select.disabled) select.focus();
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
        if (pending || select.disabled || !form.reportValidity()) return;

        pending = true;
        submitBtn.disabled = true;
        submitBtn.textContent = "Adicionando…";
        errorEl.hidden = true;
        form.setAttribute("aria-busy", "true");

        try {
            var response = await fetch(form.action, {
                method: "POST",
                body: new FormData(form),
            });
            if (!response.ok) throw new Error("HTTP " + response.status);
            window.location.reload();
        } catch (error) {
            errorEl.textContent = "Não foi possível adicionar a especialidade. Verifique se ela já está vinculada ao professor e tente novamente.";
            errorEl.hidden = false;
        } finally {
            pending = false;
            submitBtn.disabled = false;
            submitBtn.textContent = "Adicionar especialidade";
            form.removeAttribute("aria-busy");
        }
    });
}
