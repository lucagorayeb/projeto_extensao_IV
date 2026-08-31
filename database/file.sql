-- Active: 1787970618063@@127.0.0.1@3306
CREATE TABLE disciplinas(
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    disciplina TEXT NOT NULL
)

CREATE TABLE formato_disciplina(
    id_formato_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    formato_disciplina TEXT NOT NULL
)

CREATE TABLE professores(
    id_professores INTEGER PRIMARY KEY AUTOINCREMENT,
    professores TEXT NOT NULL
)

CREATE TABLE salas(
    id_salas INTEGER PRIMARY KEY AUTOINCREMENT,
    sala TEXT NOT NULL
)