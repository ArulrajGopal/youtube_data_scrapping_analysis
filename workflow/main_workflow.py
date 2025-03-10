from utility import *

channel_details_lst = extract_channel_details(channel_id_dict)

for response in channel_details_lst:
    load_dyanmo_db("channel_raw","primary_key",response)


