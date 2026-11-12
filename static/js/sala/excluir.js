export function initDeleteSala(showToast) {
    var modalEl = document.getElementById("delete-sala-modal");
    var list = document.querySelector("[data-sala-list]");
    if (!modalEl || !list || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var trigger = null;
    var card = null;

    list.addEventListener("click", function (event) {
        var btn = event.target.closest('[data-action="delete"][data-entity="sala"]');
        if (!btn || btn.disabled || trigger) return;
        trigger = btn;
        card = btn.closest("[data-sala-card]");
        modalEl.querySelector("[data-delete-name]").textContent = card.dataset.nome;
        modal.show();
    });

    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-delete-cancel]").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger && trigger.isConnected) trigger.focus();
        else document.getElementById("sala-nome").focus();
        trigger = null;
        card = null;
    });

    var confirmBtn = modalEl.querySelector("[data-confirm-delete]");
    confirmBtn.addEventListener("click", async function () {
        if (!card) return;
        var data = new FormData();
        data.append("id", card.dataset.id);
        confirmBtn.disabled = true;
        try {
            var response = await fetch(confirmBtn.dataset.deleteUrl, {
                method: "DELETE",
                body: data,
            });
            if (!response.ok) throw new Error("HTTP " + response.status);
            window.location.reload();
        } catch (error) {
            showToast("Não foi possível enviar a solicitação de exclusão. Tente novamente.", "error");
        } finally {
            confirmBtn.disabled = false;
        }
    });
}
