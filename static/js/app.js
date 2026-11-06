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
     Abas de cadastro + hash da URL
     ------------------------------------------------------------------------ */
  function initCadastroTabs() {
    var triggers = document.querySelectorAll('[data-bs-toggle="pill"]');
    if (!triggers.length) return;

    var hash = window.location.hash.replace("#", "");
    if (["salas", "professores", "turmas"].indexOf(hash) !== -1) {
      var trigger = document.querySelector(
        '[data-bs-toggle="pill"][data-bs-target="#pane-' + hash + '"]'
      );
      if (trigger && window.bootstrap && window.bootstrap.Tab) {
        window.bootstrap.Tab.getOrCreateInstance(trigger).show();
      }
    }

    triggers.forEach(function (trigger) {
      trigger.addEventListener("shown.bs.tab", function (event) {
        var target = event.target.getAttribute("data-bs-target") || "";
        var name = target.replace("#pane-", "");
        if (window.history && window.history.replaceState) {
          window.history.replaceState(null, "", "#" + name);
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
     Calendário da home (semana / dia)
     ------------------------------------------------------------------------ */
  var DAY_LABELS = [
    "Segunda-feira, 2 de novembro",
    "Terça-feira, 3 de novembro",
    "Quarta-feira, 4 de novembro",
    "Quinta-feira, 5 de novembro",
    "Sexta-feira, 6 de novembro",
    "Sábado, 7 de novembro",
  ];

  function scrollCalendarToEvening(root) {
    if (!root) return;
    root.querySelectorAll(".calendar-body").forEach(function (el) {
      el.scrollTop = Math.max(0, 512);
    });
  }

  function initCalendar() {
    var week = document.getElementById("cal-week");
    var day = document.getElementById("cal-day");
    if (!week || !day) return;

    var viewButtons = document.querySelectorAll(".cal-view-btn");
    var dayNav = document.querySelector(".calendar-day-nav");
    var dayLabel = document.getElementById("cal-day-label");
    var weekLabel = dayLabel ? dayLabel.getAttribute("data-week-label") : "";
    var panels = day.querySelectorAll("[data-day-panel]");
    var currentDay = 3;

    panels.forEach(function (panel) {
      if (panel.getAttribute("data-today") === "true") {
        currentDay = Number(panel.getAttribute("data-day-panel"));
      }
    });

    function showDayPanel(index) {
      currentDay = (index + panels.length) % panels.length;
      panels.forEach(function (panel) {
        var active = Number(panel.getAttribute("data-day-panel")) === currentDay;
        panel.classList.toggle("d-none", !active);
      });

      if (dayLabel) {
        dayLabel.textContent = DAY_LABELS[currentDay] || "";
      }

      var activePanel = day.querySelector(
        '[data-day-panel="' + currentDay + '"]'
      );
      scrollCalendarToEvening(activePanel);
    }

    function setView(view) {
      var isWeek = view === "week";
      week.classList.toggle("d-none", !isWeek);
      day.classList.toggle("d-none", isWeek);

      viewButtons.forEach(function (btn) {
        btn.classList.toggle("active", btn.getAttribute("data-view") === view);
        btn.setAttribute(
          "aria-pressed",
          btn.getAttribute("data-view") === view ? "true" : "false"
        );
      });

      if (dayNav) {
        dayNav.classList.toggle("d-none", isWeek);
      }

      if (isWeek) {
        if (dayLabel) dayLabel.textContent = weekLabel;
        scrollCalendarToEvening(week);
      } else {
        showDayPanel(currentDay);
      }
    }

    viewButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        setView(btn.getAttribute("data-view"));
      });
    });

    var prev = document.querySelector(".cal-prev-day");
    var next = document.querySelector(".cal-next-day");

    if (prev) {
      prev.addEventListener("click", function () {
        showDayPanel(currentDay - 1);
      });
    }

    if (next) {
      next.addEventListener("click", function () {
        showDayPanel(currentDay + 1);
      });
    }

    setView("week");
  }

  /* ------------------------------------------------------------------------
     Modal de confirmação de exclusão
     ------------------------------------------------------------------------ */
  function initDeleteModal() {
    var modalEl = document.getElementById("delete-modal");
    if (!modalEl || !window.bootstrap) return;

    var modal = new window.bootstrap.Modal(modalEl);
    var titleEl = modalEl.querySelector(".modal-title");
    var descEl = modalEl.querySelector("[data-delete-description]");
    var confirmBtn = modalEl.querySelector("[data-confirm-delete]");
    var pending = null;

    document.querySelectorAll("[data-delete-title]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        pending = btn.closest("[data-deletable]");
        if (titleEl) titleEl.textContent = btn.getAttribute("data-delete-title");
        if (descEl) descEl.textContent = btn.getAttribute("data-delete-description") || "";
        modal.show();
      });
    });

    if (confirmBtn) {
      confirmBtn.addEventListener("click", function () {
        if (pending) {
          pending.remove();
          pending = null;
          showToast("Registro removido.", "success");
        }
        modal.hide();
      });
    }
  }

  /* ------------------------------------------------------------------------
     Formulários de demonstração
     ------------------------------------------------------------------------ */
  function initDemoForms() {
    document.querySelectorAll("[data-demo-form]").forEach(function (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        event.stopPropagation();

        var required = form.querySelectorAll("[required]");
        var invalid = false;
        required.forEach(function (field) {
          if (!field.value.trim()) {
            field.classList.add("is-invalid");
            invalid = true;
          } else {
            field.classList.remove("is-invalid");
          }
        });

        if (invalid) {
          showToast("Preencha os campos obrigatórios.", "error");
          return;
        }

        showToast(form.getAttribute("data-success") || "Registro salvo.", "success");
        form.reset();

        var submit = form.querySelector('[type="submit"]');
        if (submit) {
          var original = submit.getAttribute("data-label") || submit.textContent;
          submit.setAttribute("data-label", original);
          setTimeout(function () {
            submit.innerHTML = original;
          }, 0);
        }
      });
    });
  }

  /* ------------------------------------------------------------------------
    Inicialização
     ------------------------------------------------------------------------ */
  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initCadastroTabs();
    initCalendar();
    initDeleteModal();
    initDemoForms();

    // Abre a grade já no período noturno, onde está a maioria das aulas.
    var calendar = document.getElementById("cal-week");
    if (calendar) {
      scrollCalendarToEvening(calendar);
    }
  });
})();
