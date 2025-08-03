from datetime import datetime
import pandas as pd
from config import *
from utility import *

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


def convert_json_to_pandas_df(data):
    records = []
    for entry in data:
        item = entry['items'][0]
        snippet = item['snippet']
        stats = item['statistics']
        uploads = item['contentDetails']['relatedPlaylists'].get('uploads', '')
        
        records.append({
            'channel_id': entry['channel_id'],
            'title': snippet.get('title', ''),
            'description': snippet.get('description', ''),
            'updated_time': entry['updated_time'],
            'load_dt': int(entry['load_dt']),
            'uploads': uploads,
            'videocount': int(stats.get('videoCount', 0)),
            'viewcount': int(stats.get('viewCount', 0)),
            'subscriberCount': int(stats.get('subscriberCount', 0)),
            'publishedAt': snippet.get('publishedAt', '')
        })

    # Create DataFrame
    df = pd.DataFrame(records)
    return df


channel_details_lst = extract_channel_details(channel_id_dict)
print("channels details extracted successfully!")

for response in channel_details_lst:
    load_dyanmo_db("channel_raw",response)
print("channels details loaded into dynamoDB successfully!")


json_data = read_dyanmo_db("channel_raw")
print("data scanned from dynamoDB successfully!")


df = convert_json_to_pandas_df(json_data)
print("data converted to pandas df successfully!")

load_to_sql(df, "channel_details")
print("data loaded into postgresql table successfully!")

