CREATE TABLE [dbo].[DimSupplier]
(
    [SupplierId] NVARCHAR (50) NOT NULL,
    [SupplierName] NVARCHAR (50) NULL,
    CONSTRAINT [PK_DimSupplier] PRIMARY KEY CLUSTERED ([SupplierId] ASC)
);