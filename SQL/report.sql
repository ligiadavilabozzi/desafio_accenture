-- Para saber os clientes fraudados nas entradas e a data do fraude: 
SELECT  C.nome, C.telefone, E1.valor, E1.data, E2.valor, E2.data 
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 
INNER JOIN clientes C
ON E1.cliente_id = C.cliente_id
ORDER BY E1.cliente_id

-- Para saber os clientes fraudados nas saídas e a data do fraude: 
SELECT  C.nome, C.telefone, S1.valor, S1.data, S2.valor, S2.data 
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 
INNER JOIN clientes C
ON S1.cliente_id = C.cliente_id
ORDER BY S1.cliente_id

--------------------------------------------------------------------------------------------------------------------

--Para saber quantos clientes possuem fraude na entrada
SELECT COUNT(DISTINCT(E1.cliente_id))
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id and 
DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 

--Para saber quantos clientes possuem fraude na saída
SELECT COUNT(DISTINCT(S1.cliente_id))
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id and 
DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 



--------------------------------------------------------------------------------------------------------------------

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



