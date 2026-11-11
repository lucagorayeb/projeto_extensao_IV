import { initDeleteRequests } from "./professor/excluir.js";
import { initAddSpecialty } from "./professor/adicionar-especialidade.js";
import { initViewProfessor } from "./professor/visualizar.js";
import { initEditProfessor } from "./professor/editar.js";
import { initCreateSala } from "./sala/cadastrar.js";
import { initViewSala } from "./sala/visualizar.js";
import { initEditSala } from "./sala/editar.js";
import { initDeleteSala } from "./sala/excluir.js";

/*==========================================================================
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

  /*------------------------------------------------------------------------
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


  /*------------------------------------------------------------------------
    Inicialização
    ------------------------------------------------------------------------ */
  function initApp() {
    initTheme();
    initDeleteRequests(showToast);
    initAddSpecialty();
    initViewProfessor();
    initEditProfessor();
    initCreateSala(showToast);
    initViewSala();
    initEditSala(showToast);
    initDeleteSala(showToast);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initApp, { once: true });
  } else {
    initApp();
  }
})();
