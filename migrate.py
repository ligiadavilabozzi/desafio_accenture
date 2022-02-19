from os.path import exists
import time


def lerArquivoClientes(id=1, contador=1):
    arquivoCliente = open(f"./csv/clients-00{id}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo clients-00{id}.csv ===== ")
    time.sleep(2)

    while True:
        contador += 1
        linha = arquivoCliente.readline()
        if not linha:
            break
        print("Linha {}: {}".format(contador, linha.strip()))
    arquivoCliente.close()

    if exists(f"./csv/clients-00{(id+1)}.csv"):
        lerArquivoClientes(id+1, contador)


def lerArquivoTransactionIn(id=1, contador=1):
    arquivoTransaction = open(
        f"./csv/transaction-in-00{id}.csv", "r", encoding="utf-8")
    print(f"===== lendo arquivo transaction-in-00{id}.csv ===== ")
    time.sleep(2)

    while True:
        contador += 1
        linha = arquivoTransaction.readline()
        if not linha:
            break
        print("Linha {}: {}".format(contador, linha.strip()))
    arquivoTransaction.close()

    if exists(f"./csv/transaction-in-00{(id+1)}.csv"):
        lerArquivoTransactionIn(id+1, contador)


def lerArquivoTransactionOut(id=1, contador=1):
    #id = str.zfill(3)
    # .rjust(3, '0')
    id_str = str(id)
    #id = f'{id_str.zfill(3)}'
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


lerArquivoClientes()
time.sleep(2)
lerArquivoTransactionIn()
time.sleep(2)
lerArquivoTransactionOut()
