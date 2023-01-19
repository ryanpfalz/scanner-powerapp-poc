CREATE TABLE [dbo].[DimProduct]
(
    [ProductId] NVARCHAR (50) NOT NULL,
    [ProductName] NVARCHAR (50) NULL,
    CONSTRAINT [PK_DimProduct] PRIMARY KEY CLUSTERED ([ProductId] ASC)
);