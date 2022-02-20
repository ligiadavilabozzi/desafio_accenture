from os.path import exists
import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I882R5G;DATABASE=inconsistencia;Trusted_Connection=yes;')
cursor = connection.cursor()


def lerArquivoClientes(id=1):
    id_str = str(id)
    arquivo = open(
        f"./csv/clients-{id_str.zfill(3)}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo clients-{id_str.zfill(3)}.csv ===== ")

    while True:
        linha = arquivo.readline()
        if linha.strip() == "id;nome;email;data_cadastro;telefone":
            continue
        elif not linha:
            break
        else:
            linha_array = linha.strip().split(sep=";")
            linha_array[0] = int(linha_array[0])
            linha_tupla = tuple(linha_array)
            cursor.execute(
                "insert into clientes(cliente_id, nome, email, data_cadastro, telefone) values (?,?,?,?,?)", linha_tupla)
            connection.commit()
    arquivo.close()

    if exists(f"./csv/clients-{str(id+1).zfill(3)}.csv"):
        lerArquivoClientes(id+1)


def lerArquivoEntradas(id=1):
    id_str = str(id)
    arquivo = open(
        f"./csv/transaction-in-{id_str.zfill(3)}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo transaction-in-{id_str.zfill(3)}.csv ===== ")

    while True:
        linha = arquivo.readline()
        if linha.strip() == "id;cliente_id;valor;data":
            continue
        elif not linha:
            break
        else:
            linha_array = linha.strip().split(sep=";")
            linha_array[0] = int((linha_array[0]))
            linha_tupla = tuple(linha_array)
            cursor.execute(
                "insert into entradas(entrada_id, cliente_id, valor, data_hora) values (?,?,?,?)", linha_tupla)
            connection.commit()
    arquivo.close()

    if exists(f"./csv/transaction-in-{str(id+1).zfill(3)}.csv"):
        lerArquivoEntradas(id+1)


def lerArquivoSaidas(id=1):
    id_str = str(id)
    arquivo = open(
        f"./csv/transaction-out-{id_str.zfill(3)}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo transaction-out-{id_str.zfill(3)}.csv ===== ")

    while True:
        linha = arquivo.readline()
        if linha.strip() == "id;cliente_id;valor;data":
            continue
        elif not linha:
            break
        else:
            linha_array = linha.strip().split(sep=";")
            linha_array[0] = int(linha_array[0])
            linha_tupla = tuple(linha_array)
            cursor.execute(
                "insert into saidas(saida_id, cliente_id, valor, data_hora) values (?,?,?,?)", linha_tupla)
            connection.commit()
    arquivo.close()

    if exists(f"./csv/transaction-out-{str(id+1).zfill(3)}.csv"):
        lerArquivoSaidas(id+1)


lerArquivoClientes()
lerArquivoEntradas()
lerArquivoSaidas()

cursor.close()
connection.close()

'''
from os.path import exists
import pandas as pd


def lerArquivoClientes(id=1):
    data = pd.read_csv(f"./csv/clients-00{id}.csv", sep=";", encoding="utf-8")
    df = pd.DataFrame(data)

    while True:
        for row in df.itertuples(index=False):
            print(row)
        if not row:
            break
    data.close()

    if exists(f"./csv/clients-00{(id+1)}.csv"):
        lerArquivoClientes(id+1)

lerArquivoClientes()
'''

'''
def lerArquivoTransactionIn(id=1, contador=1):
    arquivoTransaction = open(
        f"./csv/transaction-in-00{id}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo transaction-in-00{id}.csv ===== ")
    time.sleep(2)



    if exists(f"./csv/transaction-in-00{(id+1)}.csv"):
        lerArquivoTransactionIn(id+1, contador)


def lerArquivoTransactionOut(id=1, contador=1):
    # id = str.zfill(3)
    # .rjust(3, '0')
    id_str = str(id)
    # id = f'{id_str.zfill(3)}'
    arquivoTransaction = open(
        f"./csv/transaction-out-{id_str.zfill(3)}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo transaction-out-{id_str.zfill(3)}.csv ===== ")
    time.sleep(2)

    while True:
        contador += 1
        linha = arquivoTransaction.readline()
        if not linha:
            break
        print("Linha {}: {}".format(contador, linha.strip()))
    arquivoTransaction.close()

    if exists(f"./csv/transaction-out-{str(id+1).zfill(3)}.csv"):
        lerArquivoTransactionOut(id+1, contador)

'''

'''
time.sleep(2)
lerArquivoTransactionIn()
time.sleep(2)
lerArquivoTransactionOut()
'''
