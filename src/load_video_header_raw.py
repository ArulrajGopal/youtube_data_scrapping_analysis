from datetime import datetime
from config import *
from utility import *


def get_video_header(playlist_id):
  video_response_lst = []
  request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id)
  response = request.execute()
  
  video_response_extract = response['items']

  for i in video_response_extract:
    video_response_lst.append(i)


  next_page_token = response.get('nextPageToken')
  more_pages = True

  while more_pages:
    if next_page_token is None:
      more_pages = False
    else:
        request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults = 50, pageToken = next_page_token)
        response = request.execute()

        video_response_extract = response['items']

        for i in video_response_extract:
            video_response_lst.append(i)

        next_page_token = response.get('nextPageToken')

  return video_response_lst



def get_video_header_raw(channel_playlist_list):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    video_response_list = []
    total_playlists = len(channel_playlist_list)
    progress = 0
    for playlst in channel_playlist_list:
        video_response_lst = get_video_header(playlst)

        for item in video_response_lst:
                temp_dic = {}
                temp_dic["video_id"] = item["contentDetails"]["videoId"]
                temp_dic["response"] = item
                temp_dic["playlist_id"] = playlst
                temp_dic["load_dt"] = current_date
                temp_dic["updated_time"] = str(datetime.now())
                video_response_list.append(temp_dic)
        progress += 1
        print(f"Progress: {progress}/{total_playlists} playlists processed.")
    return video_response_list


df = read_from_sql("channel_details")
playlist_id_list = df['uploads'].tolist()
# playlist_id_list = ["UUYRB8kDbaW6a1Gufr_qwVTA","UUoxNE6QEFUAdKuqvjT-kNwA"]


video_header_list = get_video_header_raw(playlist_id_list)
print("video header list extracted successfully!")

total_videos = len(video_header_list)
progress = 0
for response in video_header_list:
    progress += 1
    print(f"Progress: {progress}/{total_videos} videos header data loaded into dynamodb successfully!.")
    load_dyanmo_db("video_raw",response)
print("all video header data loaded into dynamoDB successfully!")



