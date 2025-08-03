from config import *
import pandas as pd
from sqlalchemy import create_engine


def load_dyanmo_db(table_name,value):
    table = dynamodb.Table(table_name)
    table.put_item(Item=value)

def read_dyanmo_db(table_name):
    table = dynamodb.Table(table_name)
    response = table.scan()
    return response

def load_to_sql(df, table_name):
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"data loaded in {table_name} successfully.")


def read_from_sql(table_name):
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    df = pd.read_sql_table(table_name, engine)
    return df



