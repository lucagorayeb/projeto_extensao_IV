# Engetec — Painel de horários (HTML + Bootstrap 5)

Versão estática do layout React do projeto, convertida para HTML, CSS e JavaScript com **Bootstrap 5**.

> O código React original em `frontend/` foi mantido intacto.

## Como abrir

Não precisa de build. Basta abrir o arquivo `index.html` no navegador ou servir a pasta com um servidor simples:

```bash
# na raiz do projeto
python3 -m http.server 8080 --directory html-bootstrap
```

Depois acesse <http://localhost:8080>.

> Bootstrap 5 e Bootstrap Icons estão incluídos localmente em `assets/vendor/`, então o layout funciona offline. As fontes Inter e Source Serif 4 são carregadas via Google Fonts; sem internet, o navegador usa as fontes de fallback do sistema.

## Páginas

| Arquivo | Tela |
| --- | --- |
| `index.html` | Painel (estatísticas, calendário semanal/diário, próximas aulas e conflitos) |
| `hoje.html` | Aulas de hoje em cards |
| `semana.html` | Grade semanal em tabela (desktop) e seletor de dia (mobile) |
| `cadastro.html` | Cadastro de salas, professores e turmas |

## O que está funcionando

- Navegação entre as páginas pela sidebar (desktop) e barra inferior (mobile).
- Alternância entre tema claro e escuro, com preferência salva no `localStorage`.
- Calendário da home alternando entre **Semana** e **Dia**, com navegação entre os dias.
- Abas de cadastro (Salas, Professores e Turmas) com suporte a hash (`cadastro.html#salas`, `#professores`, `#turmas`).
- Modal de confirmação de exclusão (demonstrativo) e toasts de formulário.
- Layout responsivo (mobile-first), seguindo os breakpoints do layout original.

## Estrutura

```
html-bootstrap/
├── index.html
├── hoje.html
├── semana.html
├── cadastro.html
├── README.md
└── assets/
    ├── favicon.svg
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── app.js
    └── vendor/
        ├── bootstrap.min.css
        ├── bootstrap.bundle.min.js
        ├── bootstrap-icons.min.css
        └── fonts/
            ├── bootstrap-icons.woff
            └── bootstrap-icons.woff2
```

## Observações

- Os dados (salas, professores e turmas) foram copiados de `frontend/src/mocks/seed.ts`.
- Os formulários e botões de exclusão são demonstrativos: não persistem dados, pois esta versão é somente a camada visual em HTML/Bootstrap.
- O calendário usa posicionamento absoluto por horário, como no componente React `event-layer`, inclusive com o bloco `+N` para aulas simultâneas que não cabem nas colunas visíveis.
- Cores, tipografia, espaçamentos e componentes foram mapeados a partir do tema definido em `frontend/src/index.css`.
