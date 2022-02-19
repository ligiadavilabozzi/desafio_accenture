CREATE TABLE clientes (
	cliente_id integer NOT NULL PRIMARY KEY ,
	nome varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	data_cadastro datetime NOT NULL,
	telefone varchar(255) NOT NULL,
)
GO

CREATE TABLE entradas (
	entrada_id integer NOT NULL PRIMARY KEY,
	cliente_id integer NOT NULL 
		FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
	valor float NOT NULL,
	data_hora datetime NOT NULL,
)
GO

CREATE TABLE saidas (
	saida_id integer NOT NULL,
	cliente_id integer NOT NULL
		FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
	valor float NOT NULL,
	data_hora datetime NOT NULL,
)
GO

