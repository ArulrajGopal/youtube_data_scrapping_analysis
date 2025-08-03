from datetime import datetime
import pandas as pd
from config import *
from utility import *


def get_video_header(playlist_id):
  video_response_lst = []
  request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id)
  response = request.execute()
  
  for i in range(len(response['items'])):
    video_response_lst.append(response)
  next_page_token = response.get('nextPageToken')
  more_pages = True

  while more_pages:
    if next_page_token is None:
      more_pages = False
    else:
        request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults = 50, pageToken = next_page_token)
        response = request.execute()

        for i in range(len(response['items'])):
          video_response_lst.append(response)

        next_page_token = response.get('nextPageToken')

  return video_response_lst



def get_video_header_raw(channel_playlist_list):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    video_response_list = []
    for playlst in channel_playlist_list:
        
        video_response_lst = get_video_header(playlst)

        for i in range(len(video_response_lst)):
            response = video_response_lst[i]["items"]
        
            for j in range(len(response)):
                temp_dic = {}
                temp_dic["video_id"] = response[j]["contentDetails"]["videoId"]
                temp_dic["response"] = response[j]
                current_time = str(datetime.now())
                temp_dic["playlist_id"] = playlst
                temp_dic["load_dt"] = current_date
                temp_dic["updated_time"] = current_time
                video_response_list.append(temp_dic)
    
    return video_response_list




df = read_from_sql("channel_details")

playlist_id_list = df['uploads'].tolist()

playlist_id_list = ["UUYRB8kDbaW6a1Gufr_qwVTA"]


video_response_list = get_video_header_raw(playlist_id_list)


count = 0
for video in video_response_list:
   print(video["video_id"])
   count += 1
   if count > 50:
         break




# for response in video_response_list:
#     load_dyanmo_db("video_raw",response)
# print("video details loaded into dynamoDB successfully!")

