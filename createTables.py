import pyodbc
import time


def createTables():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF exists entradas')
    cursor.execute('DROP TABLE IF exists saidas')
    cursor.execute('DROP TABLE IF exists clientes')

    cursor.execute(
        '''
      CREATE TABLE clientes(
    cliente_id int PRIMARY KEY, 
    nome varchar(255) NOT NULL, 
    email varchar(255) NOT NULL , 
    data_cadastro datetime NOT NULL , 
    telefone varchar(20) NOT NULL 
  )
  ''')
    connection.commit()
    time.sleep(1)
    print('Tabela "clientes" criada no banco "inconsistencia"')

    cursor.execute(
        '''
      CREATE TABLE entradas(
    id int PRIMARY KEY,
    cliente_id int NOT NULL ,
    valor decimal (25,2) NOT NULL,
    data datetime NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
    )
  ''')
    connection.commit()
    time.sleep(1)
    print('Tabela "entradas" criada no banco "inconsistencia"')

    cursor.execute(
        '''
      CREATE TABLE saidas(
    id int PRIMARY KEY,
    cliente_id int NOT NULL ,
    valor decimal (25,2) NOT NULL,
    data datetime NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
  )
  ''')
    connection.commit()
    time.sleep(1)
    print('Tabela "saídas" criada no banco "inconsistencia"')

    cursor.close()
    connection.close()

    time.sleep(1)
    print('As tabelas foram criadas com sucesso no banco de dados "inconsistencia"')
