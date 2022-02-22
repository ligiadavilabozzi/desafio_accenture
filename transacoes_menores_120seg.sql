-- Para saber o cliente e a data do fraude: 
SELECT  C.nome, C.telefone, S1.valor, S1.data, S2.valor, S2.data 
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 
INNER JOIN clientes C
ON S1.cliente_id = C.cliente_id
ORDER BY S1.cliente_id

-- Para saber o cliente e a data do fraude: 
SELECT  C.nome, C.telefone, E1.valor, E1.data, E2.valor, E2.data 
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 
INNER JOIN clientes C
ON E1.cliente_id = C.cliente_id
ORDER BY E1.cliente_id

--Para saber quantos clientes com fraude na entrada
SELECT COUNT(DISTINCT(E1.cliente_id))
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 

--Para saber quantos clientes com fraude na saída
SELECT COUNT(DISTINCT(S1.cliente_id))
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 


-- Para selecionar nome telefone e e-mail dos clientes fraudados na entrada
SELECT DISTINCT(C.nome), C.telefone, C.email
from entradas E1
inner join entradas E2 
ON E1.cliente_id = e2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 
INNER JOIN clientes C
ON E1.cliente_id = C.cliente_id
ORDER BY C.nome

-- Para selecionar nome telefone e e-mail dos clientes fraudados na saída
SELECT DISTINCT(C.nome), C.telefone, C.email, C.cliente_id
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 
INNER JOIN clientes C
ON S1.cliente_id = C.cliente_id
ORDER BY C.nome

-- Criando a tabela de fraudes na entrada
CREATE TABLE fraudes_entradas (
	id int IDENTITY(1,1) PRIMARY KEY,
	cliente_id int,
	FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
	nome varchar(255) NOT NULL, 
	telefone varchar(20) NOT NULL, 
	email varchar(255)
)

-- Inserção de clientes, nome, telefone, email na tabela de fraudes entradas:
INSERT INTO fraudes_entradas (cliente_id , nome, telefone, email)
SELECT DISTINCT(C.cliente_id), C.nome, C.telefone, C.email
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 
INNER JOIN clientes C
ON E1.cliente_id = C.cliente_id


-- Criando a tabela de fraudes na saída
CREATE TABLE fraudes_saidas (
	id int IDENTITY(1,1) PRIMARY KEY,
	cliente_id int,
	FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
	nome varchar(255) NOT NULL, 
	telefone varchar(20) NOT NULL, 
	email varchar(255)
)


-- Inserção de clientes, nome, telefone, email na tabela de fraudes saídas:
INSERT INTO fraudes_saidas(cliente_id , nome, telefone, email)
SELECT DISTINCT(C.cliente_id), C.nome, C.telefone, C.email
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 
INNER JOIN clientes C
ON S1.cliente_id = C.cliente_id
