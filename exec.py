# importação dos arquivos
from createTables import createTables
from migrate import lerArquivosClientes, lerArquivosEntradas, lerArquivosSaidas
from report import numero_clientes_entrada, numero_clientes_saida, clientes_fraudados_entrada, clientes_fraudados_saida
import time

# Lista com as opções
while True:
    print("Escolha uma opção:")
    print("1 - Criar Tabelas")
    print("2 - Inserir os dados do csv nas tabelas")
    print("3 - Gerar relatório com quantidade de clientes fraudados")
    print("4 - Gerar relatório com os dados dos clientes fraudados nas transações de entrada")
    print("5 - Gerar relatório com os dados dos clientes fraudados nas transações de saída")
    print("6 - Sair")
    print("----------------------------------------------------------------------")
    print("Digite o número da opção:")
    opcao = int(input())

    if opcao == 1:
        print("----------------------------------------------------------------------")
        print("criando as tabelas no banco de dados inconsistencia...")
        time.sleep(1)
        createTables()
        print("----------------------------------------------------------------------")
        time.sleep(1)
    if opcao == 2:
        print("----------------------------------------------------------------------")
        print("inserindo os dados na tabelas...")
        time.sleep(2)
        print("inserindo os dados na tabela de clientes...")
        time.sleep(2)
        lerArquivosClientes()
        print('Dados de clientes inseridos com sucesso na tabela clientes')
        print(
            "----------------------------------------------------------------------------")
        time.sleep(2)
        print("inserindo os dados na tabela de entradas...")
        time.sleep(2)
        lerArquivosEntradas()
        print('Dados de transações de entradas inseridos com sucesso na tabela entradas')
        print(
            "----------------------------------------------------------------------------")
        time.sleep(2)
        print("inserindo os dados na tabela de saidas...")
        time.sleep(2)
        lerArquivosSaidas()
        print('Dados de transações de saidas inseridos com sucesso na tabela saidas')
        print(
            "----------------------------------------------------------------------------")
        time.sleep(2)
    if opcao == 3:
        numero_clientes_entrada()
        numero_clientes_saida()
    if opcao == 4:
        print("----------------------------------------------------------------------")
        clientes_fraudados_entrada()
        print("----------------------------------------------------------------------")
        time.sleep(1)
    if opcao == 5:
        print("----------------------------------------------------------------------")
        clientes_fraudados_saida()
        print("----------------------------------------------------------------------")
        time.sleep(1)
    if opcao == 6:
        exit()
