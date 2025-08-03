from googleapiclient.discovery import build
from config import *


youtube =  build("youtube","v3",developerKey=youtube_api_key)


# def get_video_header(playlist_id):
#   video_response_lst = []

#   request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id)
#   response = request.execute()

#   for i in range(len(response['items'])):
#     video_response_lst.append(response)

    

#   next_page_token = response.get('nextPageToken')
#   more_pages = True

#   while more_pages:
#     if next_page_token is None:
#       more_pages = False
#     else:
#         request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults = 50, pageToken = next_page_token)
#         response = request.execute()

#         for i in range(len(response['items'])):
#           video_response_lst.append(response)

#         next_page_token = response.get('nextPageToken')

#   return video_response_lst


# def get_video_header_raw(channel_playlist_dict):
#     current_date = int(datetime.now().strftime("%Y%m%d%H"))
#     video_response_list = []
#     for playlst in channel_playlist_dict.values():
        
#         video_response_lst = get_video_header(playlst)

#         for i in range(len(video_response_lst)):
#             response = video_response_lst[i]["items"]
        
#             for j in range(len(response)):
#                 temp_dic = {}
#                 temp_dic["video_id"] = response[j]["contentDetails"]["videoId"]
#                 temp_dic["response"] = response[j]
#                 current_time = str(datetime.now())
#                 temp_dic["playlist_id"] = playlst
#                 temp_dic["load_dt"] = current_date
#                 temp_dic["updated_time"] = current_time
#                 video_response_list.append(temp_dic)
    
#     return video_response_list



# def get_video_all(channel_plylst_dic):
#     current_date = int(datetime.now().strftime("%Y%m%d%H"))
#     video_header_lst = []
#     video_details_lst = []
   
#     for playlist_id in channel_plylst_dic.values():
#         video_header_dict = get_video_header(playlist_id)

#         for video_id, video_response in video_header_dict.items():
           
#             current_time = str(datetime.now())
#             video_response["playlist_id"] = playlist_id
#             video_response["video_id"] = video_id
#             video_response["load_dt"] = current_date
#             video_response["updated_time"] = current_time
#             video_header_lst.append(video_response)

#         # video_id_list = list(video_header_dict.keys())
#         # for video in range(0, len(video_id_list), 50):
#         #     request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_list[video:video+50]))
#         #     response = request.execute()
#         #     current_time = str(datetime.now())
#         #     response["playlist_id"] = playlist_id
#         #     response["video_id"] =video
#         #     response["load_dt"] = current_date
#         #     response["updated_time"] = current_time
#         #     video_details_lst.append(response)
        
#     return video_header_lst,video_details_lst


def get_video_header(playlist_id):
  video_header_dict = {}

  request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id)
  response = request.execute()

  for i in range(len(response['items'])):
    video_header_dict[response['items'][i]['contentDetails']['videoId']] = response

  next_page_token = response.get('nextPageToken')
  more_pages = True

  while more_pages:
    if next_page_token is None:
      more_pages = False
    else:
        request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults = 50, pageToken = next_page_token)
        response = request.execute()

        for i in range(len(response['items'])):
          video_header_dict[response['items'][i]['contentDetails']['videoId']] = response

        next_page_token = response.get('nextPageToken')

  return video_header_dict


def get_video_details(video_id_lst):
  #dislikecount not available in the API
  all_video_stats = []

  for i in range(0, len(video_id_lst), 50):
    request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_lst[i:i+50]))
    response = request.execute()

    for video in response['items']:
      video_id = video['id']
      title = video['snippet']['title']
      published_date = video['snippet']['publishedAt']
      try: 
        views = video['statistics']['viewCount']
      except KeyError:
        views = 0
      try:
        likes = video['statistics']['likeCount']
      except KeyError:
        likes = 0
      try:
        comments = video['statistics']['commentCount']
      except KeyError:
        comments = 0
      duration = video['contentDetails']['duration']

      video_stats = dict(
                      video_id = video_id,
                      title = title,
                      published_date = published_date,
                      views = views,
                      likes = likes,
                      comments = comments,
                      duration = duration
                      )
      
      all_video_stats.append(video_stats)
      

  return all_video_stats




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