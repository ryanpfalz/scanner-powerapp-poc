CREATE TABLE [dbo].[FactInventory]
(
    [CodeId] NVARCHAR (50) CONSTRAINT [DEFAULT_FactInventory_CodeId] DEFAULT ((0)) NOT NULL,
    [LocationId] NVARCHAR (50) NULL,
    [ProductId] NVARCHAR (50) NULL,
    [SupplierId] NVARCHAR (50) NULL,
    [OrderId] NVARCHAR (50) NULL,
    [EmployeeId] NVARCHAR (50) NULL,
    [Quantity] INT NULL,
    [Latitude] FLOAT (53) NULL,
    [Longitude] FLOAT (53) NULL,
    [ScannedDateTime] DATETIME NULL,
    CONSTRAINT [PK_FactInventory] PRIMARY KEY NONCLUSTERED ([CodeId] ASC),
    -- PK will be a guid, which should not be clustered, another index should be set up
    CONSTRAINT [FK_FactInventory_DimOrder] FOREIGN KEY ([OrderId]) REFERENCES [dbo].[DimOrder] ([OrderId]),
    CONSTRAINT [FK_FactInventory_DimProduct] FOREIGN KEY ([ProductId]) REFERENCES [dbo].[DimProduct] ([ProductId]),
    CONSTRAINT [FK_FactInventory_DimSupplier] FOREIGN KEY ([SupplierId]) REFERENCES [dbo].[DimSupplier] ([SupplierId])
);