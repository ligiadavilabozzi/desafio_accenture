# DESAFIO ACCENTURE - DATA AZURE

## Tabela de conteúdos

**=================**

  - [Qual o desafio?](#qual-o-desafio)
  - [Objetivos](#objetivos)
  - [A Aplicação](#a-aplicação)
  - [Features](#features)
  - [Pré-requisitos](#pré-requisitos)
  - [Modelagem de entidades e relacionamentos](#modelagem-de-entidades-e-relacionamentos)
  - [Rodando a aplicação](#rodando-a-aplicação)
  - [Relatórios do Power BI](#relatórios-do-power-bi)
  - [🛠 Tecnologias](#-tecnologias)
  - [Grupo](#grupo)

### **Qual o desafio**

Desenvolver uma aplicação em Python para carga de arquivos em um banco de dados SQL e gerar relatórios estatísticos visando a descoberta de fraudes em cartão de crédito.

### **Objetivos**

Seu objetivo inicial é analisar estes arquivos criando uma base de dados relacional para fazer a carga e depois analisá-la. O cartão fraudado, será aquele que tiver movimentações abaixo de 2 minutos de espaçamento entre as transações.

### **A aplicação**
![gif exec.py](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/gifdatela.gif)

## **Features**

- [x]  Script de migração em Python
- [x]  Modelo de Entidades e Relacionamentos
- [x]  Relatórios de análise em SQL e PowerBI
- [x]  Códigos versionados no github.com

## **Pré-requisitos**

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python](https://www.python.org)
- [Git](https://git-scm.com)

Bibliotecas da aplicação: [Pyodbc](https://mkleehammer.github.io/pyodbc/), [os.path](https://docs.python.org/3/library/os.path.html), [time](https://docs.python.org/3/library/time.html)

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

## **Modelagem de entidades e relacionamentos**
![Modelagem](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/modelagem.jpeg)
## **Rodando a aplicação**

```bash
# Clone este repositório

$ git clone <[git@github.com](mailto:git@github.com):ligiadavilabozzi/desafio_accenture.git>

# No MS SQL Server crie um banco de dados chamado inconsistência e configure para o idioma inglês(Estados Unidos)

# Abra o arquivo migrate.py e createTables.py e muda o SERVER para seu servidor na linha:  
$'DRIVER={ODBC Driver 17 for SQL Server};SERVER=SEU-SERVIDOR;DATABASE=inconsistencia;Trusted_Connection=yes;') 

# Acesse a pasta do projeto no terminal/cmd 

# Gere os relatórios em Python:  
$ python exec.py

# Para rodar outros relatórios copia as queries disponíveis em tables_for_powerBI.sql e cole no MS SQL Server e rode as queries desejadas

```

## Relatórios do Power BI
### Relatório das fraudes das transações de entrada: 
![entrada](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/entrada.png)
### Relatório das fraudes das transações de saída: 
![saida](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/saida.png) 
### Relatório das diferenças entre fraudes das transações de saída: 
![diferenca](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/diferenca.png)

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
- ![badge](https://img.shields.io/badge/python-v3.9.7-blue)
- ![Server](https://img.shields.io/badge/SQL%20Server-18-yellow)
- ![PowerBI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)
- ![VS Code](https://img.shields.io/badge/Visual%20Studio-Code-blue)

## Grupo
![grupo](https://github.com/ligiadavilabozzi/desafio_accenture/blob/main/img/grupo.png)

- Ana Vitória de Souza Cruz: https://github.com/AnaVitoriaSouza
- Flávia Labanca: https://github.com/flavialabanca
- Lígia D'Ávila Bozzi: https://github.com/ligiadavilabozzi
- Lívia Lins Melo: https://github.com/livialinsmelo
- Marcia Talyta Campelo Reis: https://github.com/marciacampeloreis
- Rayana Alves: https://github.com/Rayanealves07
- Thalita Roberta Macêdo Lima:  https://github.com/thalitarmacedo

 





