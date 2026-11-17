# Recursos locais

Os arquivos abaixo são servidos pelo próprio projeto, sem consultas a CDNs no navegador.

- `fullcalendar-6.1.11.min.js`: bundle global padrão do FullCalendar 6.1.11, obtido de `https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js`.
- `fullcalendar-pt-br-6.1.11.min.js`: tradução oficial de `@fullcalendar/core` 6.1.11.
- `fullcalendar-LICENSE.md`: licença MIT do FullCalendar.
- `fonts.css` e `fonts/*.woff2`: Inter (pesos 400–700) e Source Serif 4 (pesos 500–700), obtidas do Google Fonts, com subconjuntos latino e latino estendido para suportar português.
- `fonts/INTER-OFL.txt` e `fonts/SOURCE-SERIF-4-OFL.txt`: licenças SIL Open Font License das fontes.

O bundle do FullCalendar 6 inclui os estilos e os injeta na página. Não é necessário carregar um arquivo CSS separado da biblioteca. Os ajustes visuais do projeto permanecem em `static/css/styles.css`.

Para atualizar uma biblioteca, substitua os arquivos pela versão oficial desejada, preserve sua licença e atualize as referências em `templates/components/layout.html`.
