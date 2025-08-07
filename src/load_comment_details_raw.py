from datetime import datetime
from config import *
from utility import *


def get_popular_comments(video_id):
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