document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    const titleLabel = document.getElementById('cal-title-label');
    const prevBtn = document.querySelector('.cal-prev-btn');
    const nextBtn = document.querySelector('.cal-next-btn');
    const todayBtn = document.querySelector('.cal-today-btn');
    const viewButtons = document.querySelectorAll('.cal-view-btn');
    const errorEl = document.getElementById('calendar-error');
    const initialEventsEl = document.getElementById('calendar-events');

    function updateTitle(calendar) {
        if (!titleLabel) return;
        titleLabel.textContent = calendar.view.title;
    }

    const calendar = new FullCalendar.Calendar(calendarEl, {
        locale: 'pt-br',
        initialView: 'timeGridWeek',
        headerToolbar: false,
        firstDay: 1, // Segunda-feira
        slotMinTime: '13:00:00',
        slotMaxTime: '23:00:00',
        height: 520,
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
        eventTimeFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        },
        dayHeaderFormat: {
            weekday: 'short',
            day: 'numeric'
        },
        events: function (fetchInfo, successCallback, failureCallback) {
            if (errorEl) errorEl.hidden = true;
            if (initialEventsEl) {
                try {
                    const data = JSON.parse(initialEventsEl.textContent);
                    if (!Array.isArray(data)) throw new Error('Resposta inválida do calendário');
                    successCallback(data);
                } catch (error) {
                    if (errorEl) errorEl.hidden = false;
                    failureCallback(error);
                }
                return;
            }
            successCallback([]);
        },
        eventClassNames: function (arg) {
            const extended = arg.event.extendedProps || {};
            const classes = ['cal-fc-event'];
            const disciplina = arg.event.title || '';
            let cor = 0;
            for (const letra of disciplina) cor = (cor * 31 + letra.codePointAt(0)) >>> 0;
            classes.push('cal-color-' + (cor % 5));
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
            const start = event.start ? event.start.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', hour12: false }) : '';
            const end = event.end ? event.end.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', hour12: false }) : '';
            const timeText = start && end ? `${start} – ${end}` : (arg.timeText || '');

            const card = document.createElement('div');
            card.className = 'cal-fc-card';
            function addText(className, text) {
                const span = document.createElement('span');
                span.className = className;
                span.textContent = text;
                span.title = text;
                card.appendChild(span);
            }
            addText('cal-fc-title', event.title);
            addText('cal-fc-sub', [props.sala, props.professor].filter(Boolean).join(' · '));
            addText('cal-fc-time', timeText);
            if (props.isConflict) {
                addText('cal-fc-conflict', 'Conflito de horário');
            }

            return { domNodes: [card] };
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
