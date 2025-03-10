from config import *
from utility import *
from datetime import datetime
import pandas as pd


def load_dyanmo_db(table_name,primary_key,value):
    table = dynamodb.Table(table_name)
    table.put_item(Item=value)
    record_id = value[primary_key]
    print(f"{record_id} record written into {table_name} successfully!!!")


def fetch_dynamo_data_into_pd_dataframe(table_name):
    table = dynamodb.Table(table_name)

    response = table.scan()
    data = response.get('Items', [])

    # Handle pagination
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response.get('Items', []))

    df = pd.DataFrame(data)

    return df


def extract_channel_details(channel_id_dict):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    channel_details_lst = []
    channel_plylst_dic = {}

    for channel in channel_id_dict.values():
        request =youtube.channels().list(part="snippet,contentDetails,statistics", id=channel)
        response = request.execute()
        current_time = str(datetime.now())
        response["channel_id"] = channel
        response["load_dt"] = current_date
        response["updated_time"] = current_time


        channel_details_lst.append(response)
        channel_plylst_dic[channel] = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


    return channel_details_lst, channel_plylst_dic



def get_video_header(playlist_id):
  video_id_list = []
  response_list = []

  request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id)
  response = request.execute()

  for i in range(len(response['items'])):
    video_id_list.append(response['items'][i]['contentDetails']['videoId'])
    response_list.append(response)

  next_page_token = response.get('nextPageToken')
  more_pages = True

  while more_pages:
    if next_page_token is None:
      more_pages = False
    else:
        request = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults = 50, pageToken = next_page_token)
        response = request.execute()

        for i in range(len(response['items'])):
          video_id_list.append(response['items'][i]['contentDetails']['videoId'])
          response_list.append(response)

        next_page_token = response.get('nextPageToken')

  return video_id_list,response_list



def get_video_details(video_id_lst):
  #dislikecount not available in the API
  all_video_stats = []

  for i in range(0, len(video_id_lst), 50):
    request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_lst[i:i+50]))
    response = request.execute()
    all_video_stats.append(response)

  return all_video_stats




def get_video_header(channel_plylst_dic):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    response_list_output = []
    video_id_list_output = []
   
    for playlist_id in channel_plylst_dic.values():
        video_id_list,response_list = get_video_header(playlist_id)

        for response in response_list:
            current_time = str(datetime.now())
            response["video_id"] = response['items'][response]['contentDetails']['videoId']
            response["load_dt"] = current_date
            response["updated_time"] = current_time
            response_list_output.append(response)


        for video in range(0, len(video_id_list), 50):
            request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_list[video:video+50]))
            response = request.execute()
            current_time = str(datetime.now())
            response["video_id"] =video
            response["load_dt"] = current_date
            response["updated_time"] = current_time
            video_id_list_output.append(response)
        
    return video_id_list_output,response_list_output