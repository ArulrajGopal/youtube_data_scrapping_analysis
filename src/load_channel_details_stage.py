import pandas as pd
from config import *
from utility import *

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
            'updated_time': entry['updated_time'],
            'load_dt': int(entry['load_dt']),
            'uploads': uploads,
            'videocount': int(stats.get('videoCount', 0)),
            'viewcount': int(stats.get('viewCount', 0)),
            'subscriberCount': int(stats.get('subscriberCount', 0)),
            'publishedAt': snippet.get('publishedAt', ''),
            'description': snippet.get('description', '')
        })

    # Create DataFrame
    df = pd.DataFrame(records)
    return df


json_data = read_dynamo_db("channel_raw")
print("data scanned from dynamoDB successfully!")


df = convert_json_to_pandas_df(json_data)
print("data converted to pandas df successfully!")

load_to_sql(df, "channel_details")
print("data loaded into postgresql table successfully!")

