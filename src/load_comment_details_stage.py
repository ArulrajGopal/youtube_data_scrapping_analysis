import pandas as pd
from config import *
from utility import *


def convert_json_to_pandas_df(json_data):
  rows = []
  for item in json_data:
      snippet = item.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
      rows.append({
          "comment_id": item.get("comment_id"),
          "textOriginal": snippet.get("textOriginal"),
          "likeCount": int(snippet.get("likeCount", 0)),
          "authorDisplayName": snippet.get("authorDisplayName"),
          "authorChannelUrl": snippet.get("authorChannelUrl"),
          "videoId": snippet.get("videoId"),
          "channelId": snippet.get("channelId"),
          "load_dt": int(item.get("load_dt", 0)),
          "publishedAt": snippet.get("publishedAt"),
          "updatedAt": snippet.get("updatedAt"),
          "updated_time": item.get("updated_time")         
      })

  df = pd.DataFrame(rows)
  return df

json_data = read_dynamo_db("comment_details_raw")
print("data scanned from dynamoDB successfully!")

print(json_data[0])


df = convert_json_to_pandas_df(json_data)
print("data converted to pandas df successfully!")

load_to_sql(df, "comment_details_stage")
print("data loaded into postgresql table successfully!")

