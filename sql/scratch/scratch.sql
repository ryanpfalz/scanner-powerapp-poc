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
WHERE EmployeeId LIKE '%ryanpfalz%'
-- WHERE CodeId like '%test%'

DELETE FROM dbo.FactInventory WHERE CodeId LIKE '%test%'

SELECT *
FROM dbo.[DimProduct]

-- DELETE FROM dbo.[DimProduct]

-- alter table dbo.[DimProduct]

SELECT *
FROM dbo.[DimSupplier]

SELECT *
FROM dbo.[DimOrder]

-- DELETE FROM dbo.FactInventory

--

SELECT
    i.CodeId,
    i.ProductId,
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
WHERE EmployeeId LIKE '%ryanpfalz%'

DELETE FROM dbo.FactInventory
-- DELETE FROM dbo.DimProduct