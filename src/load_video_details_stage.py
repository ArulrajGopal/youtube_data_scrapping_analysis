import pandas as pd
from config import *
from utility import *


def convert_json_to_pandas_df(video_list):
    data = []
    
    for video in video_list:
        snippet = video.get("snippet", {})
        thumbnails = snippet.get("thumbnails", {})

        # Prefer highest resolution thumbnail if available
        thumbnail_url = (
            thumbnails.get("maxres", {}).get("url") or
            thumbnails.get("high", {}).get("url") or
            thumbnails.get("medium", {}).get("url") or
            thumbnails.get("default", {}).get("url")
        )

        def to_int(value):
            try:
                return int(value)
            except (TypeError, ValueError):
                return None

        statistics = video.get("statistics", {})
        content = video.get("contentDetails", {})

        row = {
            "videoid": video.get("video_id"),
            "title": snippet.get("title"),
            "duration": content.get("duration"),
            "likecount": to_int(statistics.get("likeCount")),
            "view_count": to_int(statistics.get("viewCount")),
            "favoritecount": to_int(statistics.get("favoriteCount")),
            "commentcount": to_int(statistics.get("commentCount")),
            "channel_id": snippet.get("channelId"),
            "updated_time": video.get("updated_time"),
            "publishedAt": snippet.get("publishedAt"),
            "load_dt": to_int(video.get("load_dt")),
            "description": snippet.get("description"),
            "thumbnails_url": thumbnail_url,
            "categoryid": snippet.get("categoryId"),
            "channeltitle": snippet.get("channelTitle"),
            "tags": snippet.get("tags", [])  
        }

        data.append(row)

    return pd.DataFrame(data)



json_data = read_dynamo_db("video_details_raw")
print("data scanned from dynamoDB successfully!")


df = convert_json_to_pandas_df(json_data)
print("data converted to pandas df successfully!")

load_to_sql(df, "video_details_stage")
print("data loaded into postgresql table successfully!")

