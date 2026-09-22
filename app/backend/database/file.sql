# Tabela feita para o MySQL

CREATE TABLE disciplinas(
    id_disciplina INT PRIMARY KEY AUTOINCREMENT,
    nome_disciplina VARCHAR(50) NOT NULL,
    fk_formato_disciplina INT NOT NULL,
    carga_horaria_disciplina VARCHAR(50) NOT NULL,
    horario_inicio_disciplina DATETIME NOT NULL,
    horario_termino_disciplina DATETIME NOT NULL,
    pratica_disciplina BOOL NOT NULL, 
    especialidade_disciplina VARCHAR(50) NOT NULL,
    CONSTRAINTS fk_formato_disciplina FOREIGN KEY (fk_formato_disciplina) REFERENCES formato(id_formato),
	created_at DEFAULT CURRENT_TIMESTAMP,
	updated_at DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE formatos(
    id_formato INT PRIMARY KEY AUTOINCREMENT,
    nome_formato VARCHAR(50) NOT NULL,
	created_at DEFAULT CURRENT_TIMESTAMP,
	updated_at DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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