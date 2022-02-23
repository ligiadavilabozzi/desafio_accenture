# DESAFIO ACCENTURE - DATA AZURE

### **Qual o desafio?**

Desenvolver uma aplicação em Python para carga de arquivos em um banco de dados SQL e gerar relatórios estatísticos visando a descoberta de fraudes em cartão de crédito.

### **Objetivos:**

Seu objetivo inicial é analisar estes arquivos criando uma base de dados relacional para fazer a carga e depois analisá-la. O cartão fraudado, será aquele que tiver movimentações abaixo de 2 minutos de espaçamento entre as transações.

## Tabela de conteúdos

**=================**

- [DESAFIO ACCENTURE - DATA AZURE](#desafio-accenture---data-azure)
    - [**Qual o desafio?**](#qual-o-desafio)
    - [**Objetivos:**](#objetivos)
  - [Tabela de conteúdos](#tabela-de-conteúdos)
  - [**Features**](#features)
  - [**Pré-requisitos**](#pré-requisitos)
  - [**🎲**Modelagem de entidades e relacionamentos](#modelagem-de-entidades-e-relacionamentos)
  - [****🔃**Rodando a aplicação**](#rodando-a-aplicação)
  - [Relatórios do Power BI](#relatórios-do-power-bi)
  - [🛠 Tecnologias](#-tecnologias)
  - [Grupo](#grupo)

## **Features**

- [x]  Script de migração em Python
- [x]  Modelo de Entidades e Relacionamentos
- [x]  Relatórios de análise em SQL e PowerBI
- [x]  Códigos versionados no github.com

## **Pré-requisitos**

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

[Git](https://git-scm.com), 

[Python](https://www.python.org).

*Bibliotecas da aplicação: 

[Pyodbc]

[os.path] 

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

## **🎲**Modelagem de entidades e relacionamentos

## ****🔃**Rodando a aplicação**

```bash
# Clone este repositório

$ git clone <[git@github.com](mailto:git@github.com):ligiadavilabozzi/desafio_accenture.git>

# Acesse a pasta do projeto no terminal/cmd

# No MS SQL Server crie um banco de dados chamado inconsistência

# Abra o arquivo [createTables.py](http://createTables.py) e altere o nome SERVER para seu servidor do MS SQL Server

# Crie as tabelas principais do banco de dados

$ python createTables.py

# Popule as tabelas com os dados do cvs: 

$ python migrate.py

# Abra o SQL Server o rode as queries que estão no arquivo report.sql para gerar as tabelas de report. Neste mesmo arquivo também estão queries de select que geram relatório importantes, cada query vem como uma descrição do seu significado. 

```

## Relatórios do Power BI

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
- [Python](https://www.python.org/)
- [SQL Server]([https://nodejs.org/en/](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads))

## Grupo

- Ana Vitória de Souza Cruz:
- Flávia Labanca: https://github.com/flavialabanca
- Lígia D'Ávila Bozzi: https://github.com/ligiadavilabozzi
- Lívia Lins Melo
- Marcia Talyta Campelo Reis: https://github.com/marciacampeloreis
- Rayana Alves
- Thalita Roberta Macêdo Lima

 





