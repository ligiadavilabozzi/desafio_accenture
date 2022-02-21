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
    data_cadastro datetime, 
    telefone varchar(20) NOT NULL)
''')
connection.commit()
