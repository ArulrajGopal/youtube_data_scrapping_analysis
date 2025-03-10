from utility import *

channel_details_lst, channel_plylst_dic = extract_channel_details(channel_id_dict)
print("channels details extracted successfully!")
# for response in channel_details_lst:
#     load_dyanmo_db("channel_raw","channel_id",response)
# print("channels details loaded into dynamoDB successfully!")


video_header_lst, video_details_lst = get_video_all(channel_plylst_dic)
print("videos details extracted successfully!")

for video_header in video_header_lst:
    load_dyanmo_db("video_header_raw","video_id",video_header)

