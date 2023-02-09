CREATE TABLE [dbo].[DimOrder]
(
    [OrderId] NVARCHAR (50) NOT NULL,
    [OrderDate] DATE NULL,
    CONSTRAINT [PK_DimOrder] PRIMARY KEY CLUSTERED ([OrderId] ASC)
);