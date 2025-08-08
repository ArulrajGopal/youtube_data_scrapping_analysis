from datetime import datetime
from config import *
from utility import *

def extract_video_details(video_id_list):
  current_date = int(datetime.now().strftime("%Y%m%d%H"))
  all_video_stats = []

  for i in range(0, len(video_id_list), 50):
    request = youtube.videos().list(part="snippet,contentDetails,statistics",id=','.join(video_id_list[i:i+50]))
    response = request.execute()

    
    for item in response['items']:
      current_time = str(datetime.now())
      item['video_id'] = item.pop('id')
      item["load_dt"] = current_date
      item["updated_time"] = current_time

      all_video_stats.append(item)
  
  return all_video_stats
   
df = read_from_sql("video_header_stage")
video_id_list = df['video_id'].tolist()

video_details_lst = extract_video_details(video_id_list)
print("video details extracted successfully!")


for response in video_details_lst:
    load_dyanmo_db("video_details_raw",response,"video_id")
print("video details loaded into dynamoDB successfully!")


