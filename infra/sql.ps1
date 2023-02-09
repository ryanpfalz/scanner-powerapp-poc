# $origPath = Get-Location
# $origPath = $origPath.Path
# Set-Location $PSScriptRoot

# cd to infra

$CONFIG = Get-Content "./config.json" | ConvertFrom-Json
$SQL_ADMIN_PASS = Get-Content './pass.txt'


# Prerequisite: Azure CLI - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

# https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create
az group create --name $CONFIG.resourceGroupName --location $CONFIG.location

# https://learn.microsoft.com/en-us/cli/azure/sql/server?view=azure-cli-latest#az-sql-server-create
az sql server create --name $CONFIG.serverName --resource-group $CONFIG.resourceGroupName --location $CONFIG.location --admin-user $CONFIG.sqlAdminUser --admin-password $SQL_ADMIN_PASS

# https://learn.microsoft.com/en-us/cli/azure/sql/db?view=azure-cli-latest#az-sql-db-create
az sql db create -g $CONFIG.resourceGroupName -s $CONFIG.serverName -n $CONFIG.databaseName --service-objective "Basic" --backup-storage-redundancy "Local" # --bsr