/* ==========================================================================
   Engetec — Painel de horários
   Comportamentos da versão HTML + Bootstrap 5
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------------
     Tema claro/escuro
     ------------------------------------------------------------------------ */
  var THEME_KEY = "engetec-theme";

  function systemTheme() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);

    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      var icon = btn.querySelector("i");
      if (icon) {
        icon.className = theme === "dark" ? "bi bi-sun" : "bi bi-moon-stars";
      }
      btn.setAttribute(
        "aria-label",
        theme === "dark" ? "Ativar tema claro" : "Ativar tema escuro"
      );
      btn.setAttribute(
        "title",
        theme === "dark" ? "Ativar tema claro" : "Ativar tema escuro"
      );
    });
  }

  function initTheme() {
    var stored = null;
    try {
      stored = localStorage.getItem(THEME_KEY);
    } catch (e) {
      stored = null;
    }

    applyTheme(stored || systemTheme());

    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var current = document.documentElement.getAttribute("data-bs-theme");
        var next = current === "dark" ? "light" : "dark";
        applyTheme(next);
        try {
          localStorage.setItem(THEME_KEY, next);
        } catch (e) {
          /* armazenamento indisponível */
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
     Toasts
     ------------------------------------------------------------------------ */
  function ensureToastContainer() {
    var container = document.querySelector(".toast-container");
    if (!container) {
      container = document.createElement("div");
      container.className =
        "toast-container position-fixed bottom-0 end-0 p-3";
      document.body.appendChild(container);
    }
    return container;
  }

  function showToast(message, variant) {
    var container = ensureToastContainer();
    var toastEl = document.createElement("div");
    toastEl.className = "toast app-toast";
    toastEl.setAttribute("role", "status");
    toastEl.setAttribute("aria-live", "polite");
    toastEl.setAttribute("aria-atomic", "true");

    var icon = variant === "error" ? "bi-exclamation-circle" : "bi-check-circle";
    var color = variant === "error" ? "text-destructive" : "text-success";

    toastEl.innerHTML =
      '<div class="d-flex">' +
      '<div class="toast-body d-flex align-items-center gap-2">' +
      '<i class="bi ' + icon + " " + color + '"></i>' +
      "<span></span>" +
      "</div>" +
      '<button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Fechar"></button>' +
      "</div>";

    toastEl.querySelector("span").textContent = message;
    container.appendChild(toastEl);

    if (window.bootstrap && window.bootstrap.Toast) {
      var toast = new window.bootstrap.Toast(toastEl, { delay: 2800 });
      toastEl.addEventListener("hidden.bs.toast", function () {
        toastEl.remove();
      });
      toast.show();
    } else {
      toastEl.classList.add("show");
      setTimeout(function () {
        toastEl.remove();
      }, 2800);
    }
  }

  /* ------------------------------------------------------------------------
    Requisições de exclusão
      ------------------------------------------------------------------------ */
  function initDeleteRequests() {
    document.querySelectorAll('[data-action="delete"][data-delete-url]').forEach(function (btn) {
      btn.addEventListener("click", async function () {
        if (btn.disabled || !window.confirm("Enviar solicitação de exclusão deste registro?")) return;

        btn.disabled = true;
        var data = new FormData();
        data.append("id", btn.getAttribute("data-id"));

        try {
          var response = await fetch(btn.getAttribute("data-delete-url"), {
            method: "DELETE",
            body: data,
          });
          if (!response.ok) throw new Error("HTTP " + response.status);
          showToast("Solicitação de exclusão enviada.", "success");
        } catch (error) {
          showToast("Não foi possível enviar a solicitação de exclusão. Tente novamente.", "error");
        } finally {
          btn.disabled = false;
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
    Inicialização
     ------------------------------------------------------------------------ */
  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initDeleteRequests();
  });
})();
