import time
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

            cliente_id = int(linha_array[0])
            nome = linha_array[1]
            email = linha_array[2]
            data_cadastro = linha_array[3].removesuffix("-0300")
            telefone = linha_array[4]
            cursor.execute(
                "insert into clientes(cliente_id, nome, email, data_cadastro, telefone) values (?,?,?,?,?)", cliente_id, nome, email, data_cadastro, telefone)
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
            entrada_id = int(linha_array[0])
            cliente_id = int(linha_array[1])
            valor = linha_array[2]
            data = linha_array[3].removesuffix("-0300")
        try:
            cursor.execute(
                "insert into entradas(id, cliente_id, valor, data) values (?,?,?,?)", entrada_id, cliente_id, valor, data)
            connection.commit()
        except:
            pass
    arquivo.close()
    if exists(f"./csv/transaction-in-{str(id+1).zfill(3)}.csv"):
        lerArquivoEntradas(id+1)


def lerArquivosSaidas(id=1):
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
            saida_id = int(linha_array[0])
            cliente_id = int(linha_array[1])
            valor = float(linha_array[2])
            data_cadastro = linha_array[3].removesuffix("-0300")

        try:
            cursor.execute(
                "insert into saidas (id,cliente_id,valor,data) values (?,?,?,?)", saida_id, cliente_id, valor, data_cadastro)
            connection.commit()
        except:
            pass

    arquivo.close()

    if exists(f"./csv/transaction-out-{str(id+1).zfill(3)}.csv"):
        lerArquivosSaidas(id+1)


lerArquivoClientes()

lerArquivoEntradas()

lerArquivosSaidas()
