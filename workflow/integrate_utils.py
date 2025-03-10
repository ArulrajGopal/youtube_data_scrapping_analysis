from config import *
import pandas as pd

def load_dyanmo_db(table_name,primary_key,value):
    table = dynamodb.Table(table_name)
    table.put_item(Item=value)
    record_id = value[primary_key]
    print(f"{record_id} record written into {table_name} successfully!!!")


def fetch_dynamo_data_into_pd_dataframe(table_name):
    table = dynamodb.Table(table_name)

    response = table.scan()
    data = response.get('Items', [])

    # Handle pagination
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response.get('Items', []))

    df = pd.DataFrame(data)

    return df
