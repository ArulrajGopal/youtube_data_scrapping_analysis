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

        statistics = video.get("statistics", {})
        content = video.get("contentDetails", {})

        row = {
            "videoid": video.get("video_id"),
            "title": snippet.get("title"),
            "duration": content.get("duration"),
            "likecount": statistics.get("likeCount"),
            "view_count": statistics.get("viewCount"),
            "favoritecount": statistics.get("favoriteCount"),
            "commentcount": statistics.get("commentCount"),
            "channel_id": snippet.get("channelId"),
            "updated_time": video.get("updated_time"),
            "publishedAt": snippet.get("publishedAt"),
            "load_dt": video.get("load_dt"),
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
















# def get_video_details(video_id_lst):
#   #dislikecount not available in the API
#   all_video_stats = []

#   for i in range(0, len(video_id_lst), 50):
#     request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_lst[i:i+50]))
#     response = request.execute()

#     for video in response['items']:
#       video_id = video['id']
#       title = video['snippet']['title']
#       published_date = video['snippet']['publishedAt']
#       try: 
#         views = video['statistics']['viewCount']
#       except KeyError:
#         views = 0
#       try:
#         likes = video['statistics']['likeCount']
#       except KeyError:
#         likes = 0
#       try:
#         comments = video['statistics']['commentCount']
#       except KeyError:
#         comments = 0
#       duration = video['contentDetails']['duration']

#       video_stats = dict(
#                       video_id = video_id,
#                       title = title,
#                       published_date = published_date,
#                       views = views,
#                       likes = likes,
#                       comments = comments,
#                       duration = duration
#                       )
      
#       all_video_stats.append(video_stats)
      

#   return all_video_stats


