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


