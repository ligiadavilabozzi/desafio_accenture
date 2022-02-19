import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
cursor = connection.cursor()
# o SERVER pega logo que abre o SGBD


# inserir dados no banco
cursor.execute("insert into importacao(texto)values('um inserido no python')")
connection.commit()

# banco dados servidor
dados = cursor.execute("SELECT * from importacao")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print("----------------------------------------")
    print(f"texto: {row.texto}")

cursor.close()
connection.close()
