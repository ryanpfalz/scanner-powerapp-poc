from datetime import datetime
import random
import os
import string
import names
import json
import qrcode
import pandas as pd
import uuid
from sqlalchemy import create_engine, text
import urllib

# config
pd.set_option('display.max_columns', None)

base_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
root_folder = 'simulation'

with open(f'{base_dir}/infra/config.json') as jf:
    config = json.load(jf)

# pass.txt contains server password - file is ignored in gitignore and needs to be created locally in simulation folder
with open(f'{base_dir}/infra/pass.txt') as f:
    sql_pass = f.readlines()[0]

# server connection
server = config['serverName'] + '.database.windows.net'
database = config['databaseName']
username = config['sqlAdminUser']
driver = "ODBC Driver 18 for SQL Server"

engine_stmt = f"mssql+pyodbc://{username}:{sql_pass}@{server}/{database}?driver={urllib.parse.quote_plus(driver)}"
engine = create_engine(engine_stmt)

# locations, products, orders, and suppliers will have simple integer IDs in this demo
LOCATIONS_TO_GENERATE = 10
PRODUCTS_TO_GENERATE = 10
ORDERS_TO_GENERATE = 10
SUPPLIERS_TO_GENERATE = 10
EMPLOYEE_POOL_SIZE = 3


def df_to_sql(df, table, delete):
    try:
        if delete:
            sql = text(f'DELETE FROM {table}')
            engine.execute(sql)
        df.to_sql(table, engine, schema="dbo", if_exists='append', index=False)
        return df
    except Exception as e:
        print(e)
        return None


# def generate_locations(num_locations):
#     # num_locations = 10
#
#     address_suffixes = ['Rd.', 'St.', 'Blvd.', 'Ln.', 'Ave.']
#
#     generated_locations = [
#         f"{random.randint(1000, 9999)} {names.get_last_name()} {random.choice(address_suffixes)}"
#         for _ in range(0, num_locations)
#     ]
#
#     location_df = pd.DataFrame.from_dict(
#         {
#             'LocationId': [str(_).zfill(len(str(abs(num_locations)))) for _ in range(1, num_locations + 1)],
#             'Address': generated_locations
#         }
#     )
#     print(location_df)


def generate_products(num_products, drop_and_insert=True):
    # num_products = 10

    letters = string.ascii_uppercase

    generated_products = [
        f"widget-{''.join(random.choice(letters) for i in range(5))}"
        for _ in range(0, num_products)
    ]

    product_df = pd.DataFrame.from_dict(
        {
            'ProductId': [str(_).zfill(len(str(abs(num_products)))) for _ in range(1, num_products + 1)],
            'ProductName': generated_products
        }
    )
    # print(product_df)

    # write to sql and return df if successful
    # return df_to_sql(product_df, 'DimProduct')
    return df_to_sql(df=product_df, table='DimProduct', delete=drop_and_insert)


def generate_orders(num_orders, drop_and_insert=True):
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
            'OrderId': [str(_).zfill(len(str(abs(num_orders)))) for _ in range(1, num_orders + 1)],
            'OrderDate': generated_order_dates
        }
    )

    # write to sql and return df if successful
    return df_to_sql(df=order_df, table='DimOrder', delete=drop_and_insert)


def generate_suppliers(num_suppliers, drop_and_insert=True):
    # num_suppliers = 10

    company_suffixes = ['Ltd.', 'Corp', 'Co.', 'LLC', 'Inc.', 'Supply']
    letters = string.ascii_uppercase

    generated_suppliers = [
        f"{''.join(random.choice(letters) for i in range(3))} {random.choice(company_suffixes)}"
        for _ in range(0, num_suppliers)
    ]

    supplier_df = pd.DataFrame.from_dict(
        {
            'SupplierId': [str(_).zfill(len(str(abs(num_suppliers)))) for _ in range(1, num_suppliers + 1)],
            'SupplierName': generated_suppliers
        }
    )
    # print(supplier_df)

    # write to sql and return df if successful
    # return df_to_sql(supplier_df, 'DimSupplier')
    return df_to_sql(df=supplier_df, table='DimSupplier', delete=drop_and_insert)


def generate_random_qr(products=PRODUCTS_TO_GENERATE, suppliers=SUPPLIERS_TO_GENERATE, orders=ORDERS_TO_GENERATE,
                       show_image=True):
    # quantity can be anywhere between 1 and 30
    quantity = random.randint(1, 30)

    qr_id = str(uuid.uuid4())

    qr_data = {
        'codeId': qr_id,
        'productId': random.choice(range(1, products)),
        'supplierId': random.choice(range(1, suppliers)),
        'orderId': random.choice(range(1, orders)),
        'quantity': quantity
    }

    if show_image:
        qr = qrcode.make(qr_data)
        print(qr_data)
        qr.show()

    return qr_data


def generate_employee_emails(num_to_choose=1):
    # generate employees based on pool size and then randomly select from them until parameter # is selected

    employee_emails = [
        f"{names.get_full_name().lower().replace(' ', '')}@company.com"
        for _ in range(0, EMPLOYEE_POOL_SIZE)
    ]

    selected_emails = [random.choice(employee_emails) for _ in range(num_to_choose)]
    return selected_emails


def generate_coordinates(num_records=1):
    return pd.DataFrame([
        {
            "latitude": round(random.uniform(-90, 90), 5),
            "longitude": round(random.uniform(-180, 180), 5)
        }
        for _ in range(0, num_records)
    ])


def test_insert_fact_records(num_records=2):
    # generate QR data
    qr_data = [
        generate_random_qr(show_image=False)
        for _ in range(0, num_records)
    ]
    qr_df = pd.DataFrame(qr_data)

    # generate user data to tie to QR data (this would come from Power App client) and add as column
    employees = generate_employee_emails(num_to_choose=len(qr_df))
    qr_df['employeeId'] = employees

    # generate coordinates to tie to user data (this would come from Power App client) and merge as columns
    qr_df = pd.concat(
        [qr_df, generate_coordinates(num_records=len(qr_df))], axis=1
    )

    print(qr_data)


def main():
    # TODO remove FKs, truncate dim and fact tables, and regenerate FKs before running simulation (?)

    # generate_locations(LOCATIONS_TO_GENERATE)
    generate_products(PRODUCTS_TO_GENERATE)
    generate_orders(ORDERS_TO_GENERATE)
    generate_suppliers(SUPPLIERS_TO_GENERATE)

    generate_random_qr(PRODUCTS_TO_GENERATE, SUPPLIERS_TO_GENERATE, ORDERS_TO_GENERATE)
    # TODO generate barcode

    test_insert_fact_records()


if __name__ == '__main__':
    main()
