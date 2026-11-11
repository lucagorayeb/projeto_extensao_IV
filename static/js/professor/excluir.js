export function initDeleteRequests(showToast) {
    var modalEl = document.getElementById("delete-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    var modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    var confirmBtn = modalEl.querySelector("[data-confirm-delete]");
    var activeTrigger = null;

    function confirmDeletion(btn) {
        return new Promise(function (resolve) {
            var confirmed = false;
            var item = btn.closest(".panel");
            var title = item && item.querySelector(".list-item-title");
            modalEl.querySelector("[data-delete-name]").textContent = title
                ? title.textContent.trim()
                : "este registro";

            function onConfirm() {
                confirmed = true;
                modal.hide();
            }

            confirmBtn.addEventListener("click", onConfirm);
            modalEl.addEventListener("shown.bs.modal", function () {
                modalEl.querySelector("[data-delete-cancel]").focus();
            }, { once: true });
            modalEl.addEventListener("hidden.bs.modal", function () {
                confirmBtn.removeEventListener("click", onConfirm);
                activeTrigger = null;
                btn.focus();
                resolve(confirmed);
            }, { once: true });
            modal.show();
        });
    }

    document.querySelectorAll('[data-action="delete"][data-delete-url]').forEach(function (btn) {
        btn.addEventListener("click", async function () {
            if (btn.disabled || activeTrigger) return;
            activeTrigger = btn;
            if (!await confirmDeletion(btn)) return;

            btn.disabled = true;
            var data = new FormData();
            data.append("id", btn.getAttribute("data-id"));

            try {
                var response = await fetch(btn.getAttribute("data-delete-url"), {
                    method: "DELETE",
                    body: data,
                });
                if (!response.ok) throw new Error("HTTP " + response.status);
                window.location.reload();
            } catch (error) {
                showToast("Não foi possível enviar a solicitação de exclusão. Tente novamente.", "error");
            } finally {
                btn.disabled = false;
            }
        });
    });
}
