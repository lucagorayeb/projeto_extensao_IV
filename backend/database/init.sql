-- Esquema inicial para MySQL 8.4.
-- Este arquivo cria um banco novo; não é uma migração de bancos existentes.
-- Limite de cinco turmas por professor e conflito de professor no mesmo dia
-- são validados pelo serviço de turmas.

CREATE TABLE formato (
    id int primary key auto_increment,
    nome varchar(30) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE especialidade (
	id int primary key auto_increment,
	nome varchar(30) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

CREATE TABLE tipo_sala (
	id int primary key auto_increment,
	nome varchar(50) not null,
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);


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

CREATE TABLE disciplina_especialidade (
	id int primary key auto_increment,
	fk_disciplina int not null,
	constraint fk_disciplina foreign key (fk_disciplina) references disciplina(id),
	fk_especialidade int not null,
	constraint fk_especialidade foreign key (fk_especialidade) references especialidade(id),
	created_at timestamp not null default current_timestamp,
	updated_at timestamp not null default current_timestamp on update current_timestamp
);

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
	fk_usuario int not null,
	fk_log_action int not null,
	dado_antigo varchar(255) not null,
	dado_atual varchar(255) not null,
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp on update current_timestamp
);
