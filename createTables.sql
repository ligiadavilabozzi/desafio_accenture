drop table entradas
drop table saidas
drop table clientes


CREATE TABLE clientes(
	id int IDENTITY(1,1) PRIMARY KEY,
    cliente_id int NOT NULL UNIQUE, 
    nome varchar(255) NOT NULL, 
    email varchar(255) NOT NULL , 
    data_cadastro datetime NOT NULL , 
    telefone varchar(20) NOT NULL 
)

CREATE TABLE entradas(
	id int PRIMARY KEY,
	cliente_id int NOT NULL ,
	valor decimal (25,2) NOT NULL,
	data datetime NOT NULL,
	FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
)

CREATE TABLE saidas(
	id int PRIMARY KEY,
	cliente_id int NOT NULL ,
	valor decimal (25,2) NOT NULL,
	data datetime NOT NULL,
)