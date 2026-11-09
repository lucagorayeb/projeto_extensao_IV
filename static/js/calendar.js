document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    const titleLabel = document.getElementById('cal-title-label');
    const prevBtn = document.querySelector('.cal-prev-btn');
    const nextBtn = document.querySelector('.cal-next-btn');
    const todayBtn = document.querySelector('.cal-today-btn');
    const viewButtons = document.querySelectorAll('.cal-view-btn');

    function updateTitle(calendar) {
        if (!titleLabel) return;
        titleLabel.textContent = calendar.view.title;
    }

    const calendar = new FullCalendar.Calendar(calendarEl, {
        locale: 'pt-br',
        initialView: 'timeGridWeek',
        headerToolbar: false,
        firstDay: 1, // Segunda-feira
        hiddenDays: [0], // Oculta Domingo (seg a sáb)
        slotMinTime: '07:00:00',
        slotMaxTime: '23:00:00',
        slotDuration: '01:00:00',
        snapDuration: '00:15:00',
        allDaySlot: false,
        expandRows: false,
        nowIndicator: true,
        scrollTime: '18:00:00',
        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },
        dayHeaderFormat: {
            weekday: 'short',
            day: 'numeric'
        },
        events: function (fetchInfo, successCallback, failureCallback) {
            // Busca os eventos da API / banco de dados quando houver rota,
            // ou pode receber os eventos via chamada fetch/endpoint
            fetch('/disciplina/')
                .then(response => {
                    if (!response.ok) return [];
                    return response.json();
                })
                .then(data => {
                    if (Array.isArray(data)) {
                        successCallback(data);
                    } else {
                        successCallback([]);
                    }
                })
                .catch(() => {
                    successCallback([]);
                });
        },
        eventClassNames: function (arg) {
            const extended = arg.event.extendedProps || {};
            const classes = ['cal-fc-event'];
            if (extended.isConflict) {
                classes.push('is-conflict');
            } else if (extended.predio) {
                classes.push(extended.predio);
            }
            return classes;
        },
        eventContent: function (arg) {
            const event = arg.event;
            const props = event.extendedProps || {};
            const start = event.start ? event.start.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' }) : '';
            const end = event.end ? event.end.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' }) : '';
            const timeText = start && end ? `${start} – ${end}` : (arg.timeText || '');

            let conflictHtml = '';
            if (props.isConflict) {
                conflictHtml = '<span class="cal-fc-conflict"><i class="bi bi-exclamation-triangle"></i> Conflito de horário</span>';
            }

            return {
                html: `
                    <div class="cal-fc-card">
                        <span class="cal-fc-title" title="${event.title}">${event.title}</span>
                        <span class="cal-fc-sub" title="${props.sala || ''} · ${props.professor || ''}">${props.sala || ''}${props.professor ? ' · ' + props.professor : ''}</span>
                        <span class="cal-fc-time">${timeText}</span>
                        ${conflictHtml}
                    </div>
                `
            };
        },
        datesSet: function () {
            updateTitle(calendar);
        }
    });

    calendar.render();
    updateTitle(calendar);

    // Controles de navegação
    if (prevBtn) {
        prevBtn.addEventListener('click', function () {
            calendar.prev();
            updateTitle(calendar);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function () {
            calendar.next();
            updateTitle(calendar);
        });
    }

    if (todayBtn) {
        todayBtn.addEventListener('click', function () {
            calendar.today();
            updateTitle(calendar);
        });
    }

    // Alternar visão Semana / Dia
    viewButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            const targetView = btn.getAttribute('data-view');
            calendar.changeView(targetView);
            updateTitle(calendar);

            viewButtons.forEach(b => {
                const isActive = b === btn;
                b.classList.toggle('active', isActive);
                b.setAttribute('aria-pressed', isActive ? 'true' : 'false');
            });
        });
    });
});
