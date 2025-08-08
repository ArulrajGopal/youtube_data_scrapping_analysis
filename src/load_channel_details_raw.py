from datetime import datetime
from config import *
from utility import *

def extract_channel_details(channel_id_config):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    channel_details_lst = []

    for channel_name, channel_id, is_process in channel_id_config:
        if is_process:
            print(f"Processing channel: {channel_name} ...")
            request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
            response = request.execute()
            current_time = str(datetime.now())
            response["channel_id"] = channel_id
            response["load_dt"] = current_date
            response["updated_time"] = current_time

            channel_details_lst.append(response)

         
    return channel_details_lst

channel_details_lst = extract_channel_details(channel_id_config)
print("channels details extracted successfully!")

for response in channel_details_lst:
    load_dyanmo_db("channel_raw",response,"channel_id")
print("channels details loaded into dynamoDB successfully!")

