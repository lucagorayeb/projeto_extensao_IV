export function showErrorModal(message, { title = "Não foi possível concluir", trigger = document.activeElement } = {}) {
    const modalEl = document.getElementById("error-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) {
        window.alert(message);
        return Promise.resolve();
    }

    modalEl.querySelector("[data-error-title]").textContent = title;
    modalEl.querySelector("[data-error-message]").textContent = message;

    return new Promise(function (resolve) {
        modalEl.addEventListener("shown.bs.modal", function () {
            modalEl.querySelector("[data-error-close]").focus();
        }, { once: true });
        modalEl.addEventListener("hidden.bs.modal", function () {
            if (trigger && trigger.isConnected) trigger.focus();
            resolve();
        }, { once: true });
        window.bootstrap.Modal.getOrCreateInstance(modalEl).show();
    });
}

export async function responseErrorMessage(response) {
    // Nunca mostrar detalhes internos do servidor nem páginas HTML de erro.
    if (response.status >= 500) return "Ocorreu um erro no servidor. Tente novamente mais tarde.";
    try {
        const data = await response.json();
        const detail = typeof data === "string" ? data : data.detail || data.content || data.message;
        if (typeof detail === "string" && detail.trim()) return detail;
        if (Array.isArray(detail)) {
            const messages = detail.map(function (item) { return item.msg; }).filter(function (message) { return typeof message === "string"; });
            if (messages.length) return messages.join("\n");
        }
    } catch {
        // Respostas sem JSON recebem a mensagem padrão abaixo.
    }
    return "Não foi possível concluir a solicitação. Confira os dados e tente novamente.";
}
