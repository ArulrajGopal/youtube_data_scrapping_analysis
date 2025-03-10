from utility import *

channel_details_lst = extract_channel_details(channel_id_dict)

print("channels details extracted successfully!")

for response in channel_details_lst:
    load_dyanmo_db("channel_raw","channel_id",response)

print("channels details loaded into dynamoDB successfully!")


# df = fetch_dynamo_data_into_pd_dataframe("channel_raw")
# print(df)
