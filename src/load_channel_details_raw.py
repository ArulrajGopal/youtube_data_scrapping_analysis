from datetime import datetime
from config import *
from utility import *

def extract_channel_details(channel_id_dict):
    current_date = int(datetime.now().strftime("%Y%m%d%H"))
    channel_details_lst = []

    for channel in channel_id_dict.values():
        request =youtube.channels().list(part="snippet,contentDetails,statistics", id=channel)
        response = request.execute()
        current_time = str(datetime.now())
        response["channel_id"] = channel
        response["load_dt"] = current_date
        response["updated_time"] = current_time

        channel_details_lst.append(response)

    return channel_details_lst


channel_details_lst = extract_channel_details(channel_id_dict)
print("channels details extracted successfully!")

for response in channel_details_lst:
    load_dyanmo_db("channel_raw",response)
print("channels details loaded into dynamoDB successfully!")

