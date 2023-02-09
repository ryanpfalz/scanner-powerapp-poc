<!-- Create a pass.txt file in infra/
Python & PowerShell scripts will use config.json and pass.txt  -->

# scanner-powerapp-poc

---

| Page Type | Languages              | Key Services       | Tools      |
| --------- | ---------------------- | ------------------ | ---------- |
| Sample    | PowerShell <br> Python | Azure SQL Database | Power Apps |

---

# Setting up a QR/Barcode scanner Power App

This codebase is only a proof-of-concept, _*not*_ a production application, and should only be used to evaluate the technologies and serve as a foundational example.

## Prerequisites

-   [An Azure Subscription](https://azure.microsoft.com/en-us/free/) - for hosting cloud infrastructure
-   [Az CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) - for deploying Azure infrastructure as code
-   License for Power Platform - to log into [Power Apps](https://make.powerapps.com/) and [Power BI](https://app.powerbi.com/home)
-   [Python](https://www.python.org/downloads/) - for running simulation + Python development
-   A SQL development environment like [Azure Data Studio](https://azure.microsoft.com/en-us/products/data-studio/) - for SQL development and analysis

## Running this sample

### _*Setting up the application components*_

#### SQL Database

_Whether provisioning the SQL instance via Portal or CLI, a file called `pass.txt` needs to be created in the `infra/` folder, and the SQL server password needs to be placed in the file._

To deploy in Azure Portal:

-   Follow [this quickstart](https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal) guide.

To deploy with Az CLI:

-   Add the desired resource names and configurations in `infra/config.json`.
-   Run the script `infra/sql.ps1`.
-   This will create a [Resource Group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli#what-is-a-resource-group), [SQL Server](https://azure.microsoft.com/en-us/services/sql-database/campaign/#overview), and a [SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql).

Creating the tables:

-   In the SQL development environment (e.g., Azure Data Studio), open and run the `.sql` scripts in `sql/tables`. This will create the following tables emulating a warehouse management system:
    -   Inventory fact table
    -   Orders dimension table
    -   Product dimension table
    -   Suppliers dimension table
-   The data model can be seen in [this diagram](docs/chart.png).

#### Power Platform

-   Import the Power App from `powerapp/package.zip` into your Power Apps environment.
    -   Update the database credentials with the credentials of the database created above.

#### Simulation & Barcodes

-   The code in `simulation/main.py` is used to populate the database with simulated data and generate barcodes. In addition to creating the `pass.txt` file as stated above, the server connection variables need to be updated in the `infra/config.json` to reflect the proper SQL server credentials. Both the Python & PowerShell scripts use `config.json` and `pass.txt`.

## Architecture & Workflow

![Azure & Power Platform diagram](/docs/diagram.png)

_A diagram visually describing the components in Azure and Power Platform._

1. The developer(s) perform the following tasks...
    - Pushes code/schema updates out to the SQL instance in Azure.
    - Publishes updates to the Power App.
    - Run the simulation (`simulation/main.py`) to populate the database and generate codes.
2. Users access the scanner app via the Power App on their mobile device.
3. The Power App is used to scan QR/barcodes.
4. When codes are scanned, the data read is parsed and written to the database.

## Additional Resources

-   [Build your first canvas app with Power Apps](https://learn.microsoft.com/en-us/training/modules/build-first-canvas-app/)
