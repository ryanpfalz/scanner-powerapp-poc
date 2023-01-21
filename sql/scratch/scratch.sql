SELECT TOP (1000)
    [CodeId]
      , [ProductId]
      , [SupplierId]
      , [OrderId]
      , [EmployeeId]
      , [Quantity]
      , [Latitude]
      , [Longitude]
      , [ScannedDateTime]
FROM [dbo].[FactInventory]


SELECT *
FROM dbo.[DimProduct]

-- DELETE FROM dbo.[DimProduct]

-- alter table dbo.[DimProduct]

SELECT *
FROM dbo.[DimSupplier]

SELECT *
FROM dbo.[DimOrder]

DELETE FROM dbo.FactInventory

--

SELECT
    i.CodeId,
    p.ProductName,
    s.SupplierName,
    o.OrderDate,
    i.EmployeeId,
    i.Quantity,
    i.Latitude,
    i.Longitude,
    i.ScannedDateTime
FROM
    dbo.FactInventory i
    LEFT JOIN dbo.[DimProduct] p
    ON i.ProductId = p.ProductId
    LEFT JOIN dbo.[DimSupplier] s
    ON i.SupplierId = s.SupplierId
    LEFT JOIN dbo.[DimOrder] o
    ON i.OrderId = o.OrderId