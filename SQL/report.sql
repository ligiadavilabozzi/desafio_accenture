use inconsistencia

-- Para saber os clientes fraudados nas entradas e a data do fraude: 
SELECT C.cliente_id "ID do Cliente", C.nome Nome, E1.valor "Valor recebido", 
		cast(E1.Data as datetime2(0)) Data, E2.valor "Valor recebido", 
    cast(E2.Data as datetime2(0)) Data,
		DATEDIFF(SECOND,E1.data, E2.data) "Intervalo entre Transações (s)"
from entradas E1
inner join entradas E2 
ON E1.cliente_id = E2.cliente_id 
INNER JOIN clientes C
ON E1.cliente_id = C.cliente_id
where DATEDIFF(SECOND,E1.data, E2.data) > 0 and 
DATEDIFF(SECOND,E1.data, E2.data) < 120 
ORDER BY E1.cliente_id


-- Para saber os clientes fraudados nas saídas e a data do fraude: 
SELECT C.cliente_id "ID do Cliente", C.nome Nome, S1.valor "Valor retirado", 
		cast(S1.Data as datetime2(0)) Data, S2.valor "Valor retirado", 
		cast(S2.Data as datetime2(0)) Data,
		DATEDIFF(SECOND,S1.data, S2.data) "Intervalo entre Transações (s)"
from saidas S1
inner join saidas S2 
ON S1.cliente_id = S2.cliente_id 
INNER JOIN clientes C
ON S1.cliente_id = C.cliente_id
where DATEDIFF(SECOND,S1.data, S2.data) > 0 and 
DATEDIFF(SECOND,S1.data, S2.data) < 120 
ORDER BY S1.cliente_id

--------------------------------------------------------------------------------------------------------------------

--Para saber quantos clientes possuem fraude na entrada
SELECT COUNT(DISTINCT(E1.cliente_id)) "Número de Clientes Fraudados na Entrada"
FROM entradas E1
  INNER JOIN entradas E2
  ON E1.cliente_id = E2.cliente_id
WHERE
  DATEDIFF(SECOND,E1.data, E2.data) > 0 and
  DATEDIFF(SECOND,E1.data, E2.data) < 120

--Para saber quantos clientes possuem fraude na saída
SELECT COUNT(DISTINCT(S1.cliente_id)) "Número de Clientes Fraudados na Saída"
FROM saidas S1
  INNER JOIN saidas S2
  ON S1.cliente_id = S2.cliente_id
WHERE 
  DATEDIFF(SECOND,S1.data, S2.data) > 0 and
  DATEDIFF(SECOND,S1.data, S2.data) < 120



--------------------------------------------------------------------------------------------------------------------

-- Para selecionar nome telefone e e-mail dos clientes fraudados na entrada
SELECT DISTINCT(C.nome), C.telefone, C.email
FROM entradas E1
  INNER JOIN entradas E2
  ON E1.cliente_id = e2.cliente_id
  INNER JOIN clientes C
  ON E1.cliente_id = C.cliente_id
WHERE 
  DATEDIFF(SECOND,E1.data, E2.data) > 0 and
  DATEDIFF(SECOND,E1.data, E2.data) < 120
ORDER BY C.nome

-- Para selecionar nome telefone e e-mail dos clientes fraudados na saída
SELECT DISTINCT(C.nome), C.telefone, C.email, C.cliente_id
FROM saidas S1
  INNER JOIN saidas S2
  ON S1.cliente_id = S2.cliente_id
  INNER JOIN clientes C
  ON S1.cliente_id = C.cliente_id
WHERE
  DATEDIFF(SECOND,S1.data, S2.data) > 0 and
  DATEDIFF(SECOND,S1.data, S2.data) < 120
ORDER BY C.nome



