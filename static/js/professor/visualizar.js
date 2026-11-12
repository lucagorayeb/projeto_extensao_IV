export function initViewProfessor() {
    const modalEl = document.getElementById("view-professor-modal");
    if (!modalEl || !window.bootstrap || !window.bootstrap.Modal) return;

    const modal = window.bootstrap.Modal.getOrCreateInstance(modalEl);
    let trigger = null;
    
    // const user_id = document.getElementById('professor_id')
    // const url = user_id.getAttribute('data-url')
    // const params = new URLSearchParams({
    //         id: 1
    //     });
    // console.log(`${url}${params}`)
    // fetch(`${url}`)
    //             .then(response => response.json())
    //             .then(dados => console.log(dados))
    //             .catch(erro => console.error('Erro:', erro));
    
    document.querySelectorAll('[data-action="view"][data-entity="professor"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (btn.disabled || trigger) return;
            trigger = btn;
            modalEl.querySelector("[data-professor-id]").value = btn.getAttribute("data-id")
            modalEl.querySelector("[data-professor-name]").textContent = btn.getAttribute("data-view-name") || "Não informado";
            modalEl.querySelector("[data-professor-cpf]").textContent = btn.getAttribute("data-view-cpf") || "Não informado";

            
            
            // console.log(dados)

            modalEl.querySelector("[data-professor-specialty]").textContent = btn.getAttribute("data-view-specialty") || "Nenhuma especialidade vinculada";
            modal.show();

        });
    });



    modalEl.addEventListener("shown.bs.modal", function () {
        modalEl.querySelector("[data-view-close]").focus();
    });
    modalEl.addEventListener("hidden.bs.modal", function () {
        if (trigger) trigger.focus();
        trigger = null;
    });
}
