from config import *
from utility import *
from datetime import datetime
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
    channel_details_lst = []

    for channel in channel_id_dict.values():
        request =youtube.channels().list(part="snippet,contentDetails,statistics", id=channel)
        response = request.execute()
        current_time = str(datetime.now())
        response["channel_id"] = channel
        response["load_dt"] = current_date
        response["updated_time"] = current_time


        channel_details_lst.append(response)

    return channel_details_lst


