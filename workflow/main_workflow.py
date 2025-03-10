from utility import *

channel_details_lst, channel_plylst_dic = extract_channel_details(channel_id_dict)
print("channels details extracted successfully!")
for response in channel_details_lst:
    load_dyanmo_db("channel_raw","channel_id",response)
print("channels details loaded into dynamoDB successfully!")



video_id_list_output,response_list_output = get_video_header(channel_plylst_dic)

for response in response_list_output:
    load_dyanmo_db("video_header_raw","playlist_id",response)


# df = fetch_dynamo_data_into_pd_dataframe("channel_raw")
# print(df)
