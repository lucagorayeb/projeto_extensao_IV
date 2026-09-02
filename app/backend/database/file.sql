-- Active: 1788213744352@@127.0.0.1@3306
PRAGMA foreign_keys = ON;

CREATE TABLE disciplinas(
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    disciplina TEXT NOT NULL,
    fk_formato_disciplina INT NOT NULL,
    FOREIGN KEY (fk_formato_disciplina) REFERENCES formato_disciplina(id_formato_disciplina) 
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

DROP TABLE disciplinas;