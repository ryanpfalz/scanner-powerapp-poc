CREATE TABLE [dbo].[FactInventory]
(
    [InventoryId] INT IDENTITY(1,1) NOT NULL,
    [LocationId] NVARCHAR (50) NULL,
    [ProductId] NVARCHAR (50) NULL,
    [SupplierId] NVARCHAR (50) NULL,
    [OrderId] NVARCHAR (50) NULL,
    [EmployeeId] NVARCHAR (50) NULL,
    [Quantity] INT NULL,
    [ScannedDateTime] DATETIME2 (7) NULL,
    CONSTRAINT [PK_FactInventory] PRIMARY KEY CLUSTERED ([InventoryId] ASC),
    CONSTRAINT [FK_FactInventory_DimLocation] FOREIGN KEY ([LocationId]) REFERENCES [dbo].[DimLocation] ([LocationId]),
    CONSTRAINT [FK_FactInventory_DimOrder] FOREIGN KEY ([OrderId]) REFERENCES [dbo].[DimOrder] ([OrderId]),
    CONSTRAINT [FK_FactInventory_DimProduct] FOREIGN KEY ([ProductId]) REFERENCES [dbo].[DimProduct] ([ProductId]),
    CONSTRAINT [FK_FactInventory_DimSupplier] FOREIGN KEY ([SupplierId]) REFERENCES [dbo].[DimSupplier] ([SupplierId])
);