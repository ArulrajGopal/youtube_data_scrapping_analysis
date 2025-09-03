from config import *
import pandas as pd
from sqlalchemy import create_engine
from config import *
from utility import *

import botocore.exceptions


def read_dynamo_db(table_name):
    table = dynamodb_resource.Table(table_name)
    items = []

    response = table.scan()
    items.extend(response.get('Items', []))

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items', []))

    return items

def load_to_sql(df, table_name):
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def read_from_sql(table_name):
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    df = pd.read_sql_table(table_name, engine)
    return df



def table_exists(table_name):
    try:
        response = dynamodb_client.describe_table(TableName=table_name)
        return response["Table"]["TableStatus"]
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return None
        else:
            raise


def create_table(table_name,primary_key):
    response = dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': primary_key, 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': primary_key, 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST'  # or use ProvisionedThroughput
    )
    print(f"Creating table '{table_name}'...")

    waiter = dynamodb_client.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return "table_created"



def delete_table(table_name):
    print(f"Deleting table '{table_name}'...")
    dynamodb_client.delete_table(TableName=table_name)

    waiter = dynamodb_client.get_waiter('table_not_exists')
    waiter.wait(TableName=table_name)
    return "table_deleted"



def load_dyanmo_db(table_name,value,primary_key, is_replace=False):
    if table_exists(table_name) is None:
        print("Table not exists")
        table_creation = create_table(table_name,primary_key)
        print(table_creation)
    elif table_exists(table_name) is not None & is_replace == True:
        print("Table exists, deleting and recreating")
        delete_table(table_name)
        print("Table deleted successfully")
        print("Recreating table...")
        table_creation = create_table(table_name,primary_key)
        print(table_creation)

    table = dynamodb_resource.Table(table_name)
    table.put_item(Item=value)











