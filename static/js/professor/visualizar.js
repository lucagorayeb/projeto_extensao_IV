export function initViewProfessor() {
    const modalEl = document.getElementById("view-professor-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    const modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    const professorId = modalEl.querySelector("[data-professor-id]");
    const specialtyEl = modalEl.querySelector("[data-professor-specialty]");
    let trigger = null;
    let activeRequest = null;

    document.querySelectorAll('[data-action="view"][data-entity="professor"]').forEach(function (btn) {
        btn.addEventListener("click", async function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            professorId.value = btn.getAttribute("data-id");
            modalEl.querySelector("[data-professor-name]").textContent = btn.getAttribute("data-view-name") || "Não informado";
            modalEl.querySelector("[data-professor-cpf]").textContent = btn.getAttribute("data-view-cpf") || "Não informado";
            specialtyEl.textContent = "Carregando especialidades…";
            specialtyEl.setAttribute("aria-busy", "true");
            modal.show();

            const controller = new AbortController();
            activeRequest = controller;

            try {
                const url = new URL(professorId.dataset.url, window.location.href);
                url.pathname = url.pathname.replace(/\/[^/]+\/?$/, "/" + encodeURIComponent(professorId.value));

                const response = await fetch(url, { signal: controller.signal });
                if (!response.ok) throw new Error("HTTP " + response.status);

                const especialidades = await response.json();
                if (!Array.isArray(especialidades)) throw new Error("A rota deve retornar uma lista de especialidades.");
                if (controller.signal.aborted) return;

                specialtyEl.textContent = especialidades.length
                    ? especialidades.map(function (especialidade) { return especialidade.nome; }).join(" | ")
                    : "Nenhuma especialidade vinculada";
            } catch (error) {
                if (controller.signal.aborted) return;
                specialtyEl.textContent = "Não foi possível carregar as especialidades. Feche e abra o modal para tentar novamente.";
                console.error("Erro ao consultar especialidades do professor:", error);
            } finally {
                if (activeRequest === controller) {
                    activeRequest = null;
                    specialtyEl.removeAttribute("aria-busy");
                }
            }
        });
    });

    modalEl.addEventListener("hide.bs.modal", function () {
        if (activeRequest) activeRequest.abort();
    });
    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-view-close]").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (activeRequest) activeRequest.abort();
        activeRequest = null;
        specialtyEl.removeAttribute("aria-busy");
        if (trigger) trigger.focus();
        trigger = null;
    });
}
