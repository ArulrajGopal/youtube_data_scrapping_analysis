from config import *
from utility import *
from config import *
from datetime import datetime
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


def extract_channel_details(channel_id_dict):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    primary_key = 0

    channel_details_lst = []

    for i,j in channel_id_dict.items():
        request =youtube.channels().list(part="snippet,contentDetails,statistics", id=j)
        response = request.execute()
        response["primary_key"] = primary_key
        response["load_dt"] = current_date

        primary_key += 1

        channel_details_lst.append(response)

    return channel_details_lst