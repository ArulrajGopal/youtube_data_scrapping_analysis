from integrate_utils import *
from config import *    

read_df = fetch_dynamo_data_into_pd_dataframe("channel_details_tbl")
print(read_df)

read_df.to_sql('youtube_channels', sqlalchemy_engine, if_exists='replace', index=False)

print("Data inserted successfully!")



