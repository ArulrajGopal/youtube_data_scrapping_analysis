import pandas as pd
from config import *
from utility import *


def convert_json_to_pandas_df(response):
    data = response["Items"]
    rows = []
    for item in data:
        row = {
            'video_id': item.get('video_id'),
            'playlist_id': item.get('playlist_id'),
            'videoPublishedAt': item['response']['contentDetails'].get('videoPublishedAt'),
            'updated_time': item.get('updated_time'),
            'load_dt': item.get('load_dt')
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df['load_dt'] = df['load_dt'].astype(int)

    return df


json_data = read_dyanmo_db("video_raw")
print("data scanned from dynamoDB successfully!")

df = convert_json_to_pandas_df(json_data)
print("data converted to pandas df successfully!")


load_to_sql(df, "video_details")
print("data loaded into postgresql table successfully!")
