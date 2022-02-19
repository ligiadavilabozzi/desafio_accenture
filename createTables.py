import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
cursor = connection.cursor()


cursor.execute('DROP TABLE IF exists clientes')
cursor.execute(
    '''
CREATE TABLE clientes 
    (cliente_id integer NOT NULL PRIMARY KEY, 
    nome varchar(255) NOT NULL, 
    email varchar(255) NOT NULL, 
    data_cadastro datetime NOT NULL, 
    telefone varchar(20) NOT NULL)
''')
connection.commit()

cursor.execute('DROP TABLE IF exists entradas')
cursor.execute('''
CREATE TABLE entradas 
    (entrada_id integer NOT NULL PRIMARY KEY,
	cliente_id integer NOT NULL 
		FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
	valor float NOT NULL,
	data_hora datetime NOT NULL,
)''')
connection.commit()

cursor.execute('DROP TABLE IF exists saidas')
cursor.execute('''
CREATE TABLE saidas (
	saida_id integer NOT NULL,
	cliente_id integer NOT NULL
		FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
	valor float NOT NULL,
	data_hora datetime NOT NULL,
)
''')
connection.commit()
