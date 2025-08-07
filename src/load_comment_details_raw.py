from datetime import datetime
from config import *
from utility import *


def get_popular_comments(video_id_list):
  current_date = int(datetime.now().strftime("%Y%m%d%H"))
  all_popular_comments = []

  for video_id in video_id_list:
    request = youtube.commentThreads().list(part="snippet,replies", maxResults=100,order="relevance",videoId=video_id)
    response = request.execute()

    comments_list = response["items"]

    for comment in comments_list:
      current_time = str(datetime.now())
      comment['comment_id'] = comment.pop('id')
      comment["load_dt"] = current_date
      comment["updated_time"] = current_time
      all_popular_comments.append(comment)

  return all_popular_comments

df = read_from_sql("video_header_stage")
video_id_list = df['video_id'].tolist()

popular_comments_lst = get_popular_comments(video_id_list)
print("popular comments extracted successfully!")


for response in popular_comments_lst:
    load_dyanmo_db("comment_details_raw",response)
print("comment details loaded into dynamoDB successfully!")

