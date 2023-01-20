import pyodbc
from datetime import datetime
import random
import os
import string
import names
import json
import qrcode
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
root_folder = 'simulation'

with open(f'{base_dir}/infra/config.json') as jf:
    config = json.load(jf)

# pass.txt contains server password - file is ignored in gitignore and needs to be created locally in simulation folder
with open(f'{base_dir}/infra/pass.txt') as f:
    sqlPass = f.readlines()[0]

# server connection
server = config['serverName'] + '.database.windows.net'
database = config['databaseName']
username = config['sqlAdminUser']
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + sqlPass
)


def generate_locations(num_locations):
    # num_locations = 10

    address_suffixes = ['Rd.', 'St.', 'Blvd.', 'Ln.', 'Ave.']

    generated_locations = [
        f"{random.randint(1000, 9999)} {names.get_last_name()} {random.choice(address_suffixes)}"
        for _ in range(0, num_locations)
    ]

    location_df = pd.DataFrame.from_dict(
        {
            'LocationId': list(range(1, num_locations + 1)),
            'Address': generated_locations
        }
    )
    print(location_df)

    return


def generate_products(num_products):
    # num_products = 10

    letters = string.ascii_uppercase

    generated_products = [
        f"widget-{''.join(random.choice(letters) for i in range(5))}"
        for _ in range(0, num_products)
    ]

    product_df = pd.DataFrame.from_dict(
        {
            'ProductId': list(range(1, num_products + 1)),
            'ProductName': generated_products
        }
    )
    print(product_df)

    # TODO write to SQL

    return


def generate_orders(num_orders):
    # num_orders = 10

    date_format = '%Y-%m-%d'

    # generate and sort random dates
    generated_order_dates = [
        datetime.strftime(datetime(2022, random.randint(1, 12), random.randint(1, 28)), date_format)
        for _ in range(0, num_orders)
    ]
    generated_order_dates.sort()

    order_df = pd.DataFrame.from_dict(
        {
            'OrderId': list(range(1, num_orders + 1)),
            'OrderDate': generated_order_dates
        }
    )

    print(order_df)

    # TODO write to SQL

    return


def generate_suppliers(num_suppliers):
    # num_suppliers = 10

    company_suffixes = ['Ltd.', 'Corp', 'Co.', 'LLC', 'Inc.', 'Supply']
    letters = string.ascii_uppercase

    generated_suppliers = [
        f"{''.join(random.choice(letters) for i in range(3))} {random.choice(company_suffixes)}"
        for _ in range(0, num_suppliers)
    ]

    supplier_df = pd.DataFrame.from_dict(
        {
            'SupplierId': list(range(1, num_suppliers + 1)),
            'SupplierName': generated_suppliers
        }
    )
    print(supplier_df)

    # TODO write to SQL

    return


def generate_random_qr(products, suppliers, orders):
    # quantity can be anywhere between 1 and 30
    quantity = random.randint(1, 30)

    qr_data = {
        'productId': random.choice(range(1, products)),
        'supplierId': random.choice(range(1, suppliers)),
        'orderId': random.choice(range(1, orders)),
        'quantity': quantity
    }

    qr = qrcode.make(qr_data)
    qr.show()


def main():
    # simulation parameters
    # TODO remove FKs, truncate dim and fact tables, and regenerate FKs before running simulation

    # locations, products, orders, and suppliers will have simple integer IDs in this demo
    location_choices = 10
    product_choices = 10
    order_choices = 10
    supplier_choices = 10

    generate_locations(location_choices)
    generate_products(product_choices)
    generate_orders(order_choices)
    generate_suppliers(supplier_choices)

    generate_random_qr(product_choices, supplier_choices, order_choices)
    # TODO generate barcode


if __name__ == '__main__':
    main()