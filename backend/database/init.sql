-- Esquema inicial para MySQL 8.4.
-- Este arquivo cria um banco novo; não é uma migração de bancos existentes.
-- Limite de cinco turmas por professor e conflito de professor no mesmo dia
-- são validados pelo serviço de turmas.

SET NAMES utf8mb4;

CREATE TABLE formato (
    id int primary key auto_increment,
    nome varchar(30) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

INSERT INTO formato (nome) VALUES
	('PRESENCIAL'),
	('SÍNCRONO'),
	('ASSÍNCRONO');

CREATE TABLE tipo_sala (
	id int primary key auto_increment,
	nome varchar(50) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

INSERT INTO tipo_sala (nome) VALUES
	('LABORATÓRIO DE QUÍMICA'),
	('LABORATÓRIO DE ENGENHARIA ELÉTRICA'),
	('LABORATÓRIO DE ENGENHARIA CIVIL'),
	('LABORATÓRIO DE INFORMÁTICA'),
	('SALA DE AULA');

CREATE TABLE especialidade (
	id int primary key auto_increment,
	nome varchar(30) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

INSERT INTO especialidade (nome) VALUES
	('QUÍMICA INORGÂNICA'),
	('ANÁLISE DE CIRCUITOS'),
	('INSTALAÇÕES ELÉTRICAS PREDIAIS'),
	('MECÂNICA DOS SÓLIDOS'),
	('TECNOLOGIA DO CONCRETO'),
	('PROGRAMAÇÃO ESTRUTURADA'),
	('MODELAGEM DE DADOS'),
	('REDES DE COMPUTADORES');

CREATE TABLE disciplina (
	id int primary key auto_increment,
	nome varchar(50) not null,
	fk_formato int not null,
	constraint fk_formato foreign key (fk_formato) references formato(id),
	carga_horaria decimal(5, 2) not null,
	pratica int not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

-- Disciplinas de exemplo: formato presencial e carga horária em horas.
INSERT INTO disciplina (nome, fk_formato, carga_horaria, pratica)
SELECT dados.nome, formato.id, dados.carga_horaria, dados.pratica
FROM (
	SELECT 'QUÍMICA GERAL' AS nome, 60.00 AS carga_horaria, 1 AS pratica
	UNION ALL SELECT 'CIRCUITOS ELÉTRICOS', 60.00, 1
	UNION ALL SELECT 'INSTALAÇÕES ELÉTRICAS', 60.00, 1
	UNION ALL SELECT 'RESISTÊNCIA DOS MATERIAIS', 60.00, 0
	UNION ALL SELECT 'MATERIAIS DE CONSTRUÇÃO', 60.00, 1
	UNION ALL SELECT 'ALGORITMOS E PROGRAMAÇÃO', 60.00, 1
	UNION ALL SELECT 'BANCO DE DADOS', 60.00, 1
	UNION ALL SELECT 'REDES DE COMPUTADORES', 40.00, 1
) AS dados
JOIN formato ON formato.nome = 'PRESENCIAL';

CREATE TABLE disciplina_especialidade (
	id int primary key auto_increment,
	fk_disciplina int not null,
	constraint fk_disciplina foreign key (fk_disciplina) references disciplina(id),
	fk_especialidade int not null,
	constraint fk_especialidade foreign key (fk_especialidade) references especialidade(id),
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

INSERT INTO disciplina_especialidade (fk_disciplina, fk_especialidade)
SELECT disciplina.id, especialidade.id
FROM (
	SELECT 'QUÍMICA GERAL' AS disciplina_nome, 'QUÍMICA INORGÂNICA' AS especialidade_nome
	UNION ALL SELECT 'CIRCUITOS ELÉTRICOS', 'ANÁLISE DE CIRCUITOS'
	UNION ALL SELECT 'INSTALAÇÕES ELÉTRICAS', 'INSTALAÇÕES ELÉTRICAS PREDIAIS'
	UNION ALL SELECT 'RESISTÊNCIA DOS MATERIAIS', 'MECÂNICA DOS SÓLIDOS'
	UNION ALL SELECT 'MATERIAIS DE CONSTRUÇÃO', 'TECNOLOGIA DO CONCRETO'
	UNION ALL SELECT 'ALGORITMOS E PROGRAMAÇÃO', 'PROGRAMAÇÃO ESTRUTURADA'
	UNION ALL SELECT 'BANCO DE DADOS', 'MODELAGEM DE DADOS'
	UNION ALL SELECT 'REDES DE COMPUTADORES', 'REDES DE COMPUTADORES'
) AS vinculos
JOIN disciplina ON disciplina.nome = vinculos.disciplina_nome
JOIN especialidade ON especialidade.nome = vinculos.especialidade_nome;

CREATE TABLE professor (
	id int primary key auto_increment,
	nome varchar(30) not null,
	cpf varchar(30) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE professor_especialidade (
	id int primary key auto_increment,
	fk_professor int not null,
	fk_especialidade int not null,
	constraint fk_professor_especialidade_professor foreign key (fk_professor) references professor(id),
	constraint fk_professor_especialidade_especialidade foreign key (fk_especialidade) references especialidade(id),
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE sala (
	id int primary key auto_increment,
	nome varchar(30) not null,
	limite_alunos int not null,
	fk_tipo_sala int not null,
	constraint fk_tipo_sala foreign key (fk_tipo_sala) references tipo_sala(id),
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE dia_semana (
	id int primary key auto_increment,
	nome varchar(20) not null
);

INSERT INTO dia_semana (id, nome) VALUES
	(1, 'Segunda-feira'),
	(2, 'Terça-feira'),
	(3, 'Quarta-feira'),
	(4, 'Quinta-feira'),
	(5, 'Sexta-feira'),
	(6, 'Sábado'),
	(7, 'Domingo');

CREATE TABLE turma (
	id int primary key auto_increment,
	fk_disciplina int not null,
	fk_sala int not null,
	fk_professor int not null,
	fk_dia_semana int not null,
	horario_inicio time not null,
	horario_fim time not null,
	constraint fk_turma_disciplina foreign key (fk_disciplina) references disciplina(id),
	constraint fk_turma_sala foreign key (fk_sala) references sala(id),
	constraint fk_turma_professor foreign key (fk_professor) references professor(id),
	constraint fk_turma_dia_semana foreign key (fk_dia_semana) references dia_semana(id),
	constraint uq_turma_sala_dia unique (fk_sala, fk_dia_semana),
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE usuario (
	id int primary key auto_increment,
	nome varchar(100) not null,
	data_nascimento datetime not null,
	cpf varchar(14) not null,
	email varchar(50) not null,
	senha varchar(255) not null,
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp on update current_timestamp
);

CREATE TABLE log_action (
	id int primary key auto_increment,
	action varchar(255) not null,
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp on update current_timestamp
);

CREATE TABLE log (
	id int primary key auto_increment,
);


CREATE TABLE disciplina (
	id int primary key auto_increment,
	fk_usuario int not null,
	fk_log_action int not null,
	dado_antigo varchar(255) not null,
	dado_atual varchar(255) not null,
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp on update current_timestamp
);
