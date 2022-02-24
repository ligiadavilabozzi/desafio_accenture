# DESAFIO ACCENTURE - DATA AZURE

## Tabela de conteúdos

**=================**

  - [Qual o desafio?](#qual-o-desafio)
  - [Objetivos](#objetivos)
  - [Aplicação](#aplicação)
  - [Tabela de conteúdos](#tabela-de-conteúdos)
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

## **Rodando a aplicação**

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
- ![badge](https://img.shields.io/badge/python-v3.9.7-blue)
- ![Server](https://img.shields.io/badge/SQL%20Server-18-yellow)
- ![PowerBI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)
- ![VS Code](https://img.shields.io/badge/Visual%20Studio-Code-blue)

## Grupo

- Ana Vitória de Souza Cruz: https://github.com/AnaVitoriaSouza
- Flávia Labanca: https://github.com/flavialabanca
- Lígia D'Ávila Bozzi: https://github.com/ligiadavilabozzi
- Lívia Lins Melo: https://github.com/livialinsmelo
- Marcia Talyta Campelo Reis: https://github.com/marciacampeloreis
- Rayana Alves: https://github.com/Rayanealves07
- Thalita Roberta Macêdo Lima:  https://github.com/thalitarmacedo

 





