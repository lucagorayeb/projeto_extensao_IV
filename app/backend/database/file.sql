-- Active: 1788213744352@@127.0.0.1@3306
PRAGMA foreign_keys = ON;

CREATE TABLE disciplinas(
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_disciplina TEXT NOT NULL,
    fk_formato_disciplina INT NOT NULL,
    carga_horaria_disciplina TEXT NOT NULL,
    horario_inicio_disciplina TIME NOT NULL,
    horario_termino_disciplina TIME NOT NULL,
    pratica_disciplina INT NOT NULL, -- Simulando um bool com 0 ou 1.
    especialidade_disciplina TEXT NOT NULL,
    FOREIGN KEY (fk_formato_disciplina) REFERENCES formato(id_formato) 
);

CREATE TABLE formatos(
    id_formato INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_formato TEXT NOT NULL
);

CREATE TABLE professores(
    id_professores INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_professores TEXT NOT NULL,
    especialidade_professores TEXT NOT NULL
);

CREATE TABLE salas(
    id_salas INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_nome_sala TEXT NOT NULL,
    limite_alunos_sala INT NOT NULL,
    fk_tipo_sala INT NOT NULL,
    FOREIGN KEY (fk_tipo_sala) REFERENCES tipo_salas(id_tipo_sala)
);

CREATE TABLE tipo_salas(
    id_tipo_sala INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_sala TEXT NOT NULL
);

CREATE TABLE dados_usuarios(
    id_dados_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_dados_usuario TEXT NOT NULL,
    data_nascimento_dados_usuario DATE NOT NULL,
    cpf_dados_usuario TEXT NOT NULL
);

CREATE TABLE usuarios(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    email_usuario TEXT NOT NULL,
    senha_usuario TEXT NOT NULL,
    fk_dados_usuario INT NOT NULL,
    FOREIGN KEY (fk_dados_usuario) REFERENCES dados_usuarios(id_dados_usuario)
);