from os.path import exists
import pandas as pd
import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
cursor = connection.cursor()


def lerArquivoClientes(id=1, contador=1):
    data = pd.read_csv(f"./csv/clients-00{id}.csv", sep=";", encoding="utf-8")
    df = pd.DataFrame(data)
    print(df)

    while True:
        contador += 1
        for row in df.itertuples():
            cursor.execute('''
           insert into clientes(cliente_id, nome, email, data_cadastro, telefone)
          values(?,?,?,?,?)
        ''',
                           row[1],
                           row[2],
                           row[3],
                           row[4],
                           row[5]
                           )
        connection.commit()
        if not row:
            break

    if exists(f"./csv/clients-00{(id+1)}.csv"):
        lerArquivoClientes(id+1, contador)


lerArquivoClientes()
