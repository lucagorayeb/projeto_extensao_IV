document.addEventListener('DOMContentLoaded', function() {
    
    del_btn = document.querySelector(".delete-professor");
    url = del_btn.getAttribute("data-url");
    del_btn.addEventListener("click", function (e) {
        fetch(url);
    });


});