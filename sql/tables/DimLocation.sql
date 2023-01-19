CREATE TABLE [dbo].[DimLocation]
(
    [LocationId] NVARCHAR (50) NOT NULL,
    [Address] NVARCHAR (50) NULL,
    CONSTRAINT [PK_DimLocation] PRIMARY KEY CLUSTERED ([LocationId] ASC)
);