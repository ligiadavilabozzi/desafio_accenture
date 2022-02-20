CREATE TABLE[clientes](
    cliente_id bigint,
    nome varchar(255) NOT NULL,
    email varchar(255),
    data_cadastro datetime,
    telefone varchar(20),
    id int IDENTITY(1, 1) NOT NULL,
    CONSTRAINT[PK_CLIENTES] PRIMARY KEY CLUSTERED
    (
            [id] ASC
    ) WITH(IGNORE_DUP_KEY=OFF)

)
GO
CREATE TABLE[entradas](
    cliente_id bigint NOT NULL,
    entrada_id int NOT NULL,
    valor float NOT NULL,
    data_hora datetime NOT NULL,
    CONSTRAINT[PK_ENTRADAS] PRIMARY KEY CLUSTERED
    (
        [entrada_id] ASC
    ) WITH(IGNORE_DUP_KEY=OFF)

)
GO
CREATE TABLE[saidas](
    saida_id bigint NOT NULL,
    valor float NOT NULL,
    cliente_id int NOT NULL,
    data_hora datetime NOT NULL,

    CONSTRAINT[PK_SAIDAS] PRIMARY KEY CLUSTERED
    (
        [saida_id] ASC
    ) WITH(IGNORE_DUP_KEY=OFF)

)
GO

ALTER TABLE[entradas] WITH CHECK ADD CONSTRAINT[entradas_fk0] FOREIGN KEY([cliente_id]) REFERENCES[clientes]([cliente_id])
ON UPDATE CASCADE
GO
ALTER TABLE[entradas] CHECK CONSTRAINT[entradas_fk0]
GO

ALTER TABLE[saidas] WITH CHECK ADD CONSTRAINT[saidas_fk0] FOREIGN KEY([cliente_id]) REFERENCES[clientes]([cliente_id])
ON UPDATE CASCADE
GO
ALTER TABLE[saidas] CHECK CONSTRAINT[saidas_fk0]
GO
