import pyodbc
import time


def numero_clientes_entrada():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
    cursor = connection.cursor()

    numero_cliente_entradas = cursor.execute(
        ''' SELECT COUNT(DISTINCT(E1.cliente_id))
  FROM entradas E1
    INNER JOIN entradas E2
    ON E1.cliente_id = E2.cliente_id
  WHERE
    DATEDIFF(SECOND,E1.data, E2.data) > 0 and
    DATEDIFF(SECOND,E1.data, E2.data) < 120
  ''')
    for row in numero_cliente_entradas.fetchone():
        print("----------------------------------------------------------")
        print(f"O total de clientes fraudados na entrada foi de: {row}")
    cursor.close()
    connection.close()


def numero_clientes_saida():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
    cursor = connection.cursor()
    numero_cliente_saidas = cursor.execute(
        ''' SELECT COUNT(DISTINCT(S1.cliente_id))
    FROM saidas S1
      INNER JOIN saidas S2
      ON S1.cliente_id = S2.cliente_id
    WHERE
      DATEDIFF(SECOND,S1.data, S2.data) > 0 and
      DATEDIFF(SECOND,S1.data, S2.data) < 120
    ''')
    for row in numero_cliente_saidas.fetchone():
        print("----------------------------------------------------------")
        print(f"O total de clientes fraudados na saída foi de: {row}")
        print("----------------------------------------------------------")
    cursor.close()
    connection.close()


def clientes_fraudados_entrada():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
    cursor = connection.cursor()
    clientes_entradas = cursor.execute(
        ''' SELECT DISTINCT(C.nome), C.telefone, C.email
  FROM entradas E1
    INNER JOIN entradas E2
    ON E1.cliente_id = e2.cliente_id
    INNER JOIN clientes C
    ON E1.cliente_id = C.cliente_id
  WHERE
    DATEDIFF(SECOND,E1.data, E2.data) > 0 and
    DATEDIFF(SECOND,E1.data, E2.data) < 120
  ORDER BY C.nome
  ''')

    print("----------------------------------------------------------")
    print("Os clientes fraudados na entrada foram:")

    for row in clientes_entradas.fetchall():
        print("----------------------------------------------------------")
        print(
            f"Nome: {row[0]} \nTelefone: {row[1]} \nE-mail: {row[2]}")
        time.sleep(0.5)
    cursor.close()
    connection.close()


def clientes_fraudados_saida():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
    cursor = connection.cursor()
    clientes_saidas = cursor.execute(
        ''' SELECT DISTINCT(C.nome), C.telefone, C.email, C.cliente_id
    FROM saidas S1
      INNER JOIN saidas S2
      ON S1.cliente_id = S2.cliente_id
      INNER JOIN clientes C
      ON S1.cliente_id = C.cliente_id
    WHERE
      DATEDIFF(SECOND,S1.data, S2.data) > 0 and
      DATEDIFF(SECOND,S1.data, S2.data) < 120
    ORDER BY C.nome
  ''')

    print("----------------------------------------------------------")
    print("Os clientes fraudados na saída foram:")

    for row in clientes_saidas.fetchall():
        print("----------------------------------------------------------")
        print(
            f"Nome: {row[0]} \nTelefone: {row[1]} \nE-mail: {row[2]}")
        time.sleep(0.5)
    cursor.close()
    connection.close()
