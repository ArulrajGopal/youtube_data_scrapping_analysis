from datetime import datetime
from config import *
from utility import *


def get_popular_comments_1(video_id):
  popular_comments_lst = []

  request = youtube.commentThreads().list(part="snippet,replies", maxResults=100,order="relevance",videoId=video_id)
  response = request.execute()

  for video in response['items']:
      video_stats = dict(
                      VideoId = video['snippet']['videoId'],
                      Author = video['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                      Comment = video['snippet']['topLevelComment']['snippet']['textDisplay'],
                      CommentId = video['snippet']['topLevelComment']['id'],
                      CommentLike = video['snippet']['topLevelComment']['snippet']['likeCount'],
                      Replies = video['snippet']['totalReplyCount'],
                      PublishedAt = video['snippet']['topLevelComment']['snippet']['publishedAt'],
                      UpdatedAt = video['snippet']['topLevelComment']['snippet']['updatedAt']
                      )
      popular_comments_lst.append(video_stats)

  return popular_comments_lst

df = read_from_sql("video_header_stage")
video_id_list = df['video_id'].tolist()

video_id_list = [
   "KBLx7dFirJ4","zcPXtpdLD9o","NWGH_8gcS2Y","LWIReJELtOg","VW0uPY0FzLs","qXxgBpW5rng",
   "_BQTeU5oYac","SL7Tsb9VbZk","01zkLC4pLMA","NcVD46S7hvo","3viQfCuqbmM","y3H4ZD7H-ro",
   "hbSug7eA2nc","3cFBq3Zb7Sg","2jwGuotpiSY","A3p4BE2oTsA"
   ]


def get_popular_comments(video_id_list):
  current_date = int(datetime.now().strftime("%Y%m%d%H"))
  all_popular_comments = []

  for video_id in video_id_list:
    request = youtube.commentThreads().list(part="snippet,replies", maxResults=100,order="relevance",videoId=video_id)
    response = request.execute()

    comments_list = response["items"]

    for comment in comments_list:
      current_time = str(datetime.now())
      # comment['video_id'] = comment.pop('id')
      comment["load_dt"] = current_date
      comment["updated_time"] = current_time
      all_popular_comments.append(comment)

  return all_popular_comments

popular_comments_lst = get_popular_comments(video_id_list)
# print("popular comments extracted successfully!")
print(len(popular_comments_lst))