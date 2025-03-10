from utility import *

channel_details_lst = extract_channel_details(channel_id_dict)

for response in channel_details_lst:
    load_dyanmo_db("channel_raw","channel_id",response)


# video_id_list = []

# request = youtube.playlistItems().list(part='contentDetails',playlistId = "UUhaRiZ3h9JlLCeO2pdWkxMw")
# response = request.execute()

# with open ("sample.txt","w") as f:
#     f.write(str(response))