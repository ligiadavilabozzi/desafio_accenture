import pyodbc

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


cursor.close()
connection.close()
