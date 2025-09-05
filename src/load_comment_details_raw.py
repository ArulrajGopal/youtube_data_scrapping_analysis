from datetime import datetime
from config import *
from utility import *
from googleapiclient.errors import HttpError
import uuid

def get_popular_comments(video_id_list):
  current_date = int(datetime.now().strftime("%Y%m%d%H"))
  all_popular_comments = []

  for video_id in video_id_list:
    try:
      request = youtube.commentThreads().list(part="snippet", maxResults=number_of_comments_to_fetch,order="relevance",videoId=video_id)
      response = request.execute()

      comments_list = response["items"]

      for comment in comments_list:
        current_time = str(datetime.now())
        comment['comment_id'] = str(uuid.uuid4())
        comment["load_dt"] = current_date
        comment["updated_time"] = current_time
        all_popular_comments.append(comment)

    except HttpError as e:
        print(f"Failed to fetch comments for video ID {video_id}: {e}")


  return all_popular_comments

df = read_from_sql("video_header_stage")
video_id_list = df['video_id'].tolist()


popular_comments_lst = get_popular_comments(video_id_list)
print("popular comments extracted successfully!")

total_comments = len(popular_comments_lst)
progress = 0
for response in popular_comments_lst:
    progress += 1
    print(f"Progress: {progress}/{total_comments} comments details data loaded into dynamodb successfully!.")
    load_dyanmo_db("comment_details_raw",response,"comment_id")
print("comment details loaded into dynamoDB successfully!")

