from config import *
import pandas as pd
from sqlalchemy import create_engine
from botocore.exceptions import ClientError



def read_dynamo_db(table_name):
    table = dynamodb.Table(table_name)
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






def create_table_if_not_exists(table_name,primary_key):

    def table_exists(table_name):
        try:
            dynamodb_client.describe_table(TableName=table_name)
            print(f"Table '{table_name}' already exists.")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                return False
            else:
                raise

    if not table_exists(table_name):
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
        print(f"Table '{table_name}' is ready.")



def delete_table(name):
    try:
        print(f"Deleting table '{name}'...")
        dynamodb_client.delete_table(TableName=name)

        # Wait until the table no longer exists
        waiter = dynamodb_client.get_waiter('table_not_exists')
        waiter.wait(TableName=name)

        print(f"Table '{name}' deleted successfully.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"Table '{name}' does not exist.")
        else:
            raise



def load_dyanmo_db(table_name,value,primary_key, is_replace=False):
    if is_replace:
        delete_table(table_name)

    create_table_if_not_exists(table_name,primary_key)

    table = dynamodb_resource.Table(table_name)
    table.put_item(Item=value)












