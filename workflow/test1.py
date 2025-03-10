from integrate_utils import *
from config import *    

read_df = fetch_dynamo_data_into_pd_dataframe("channel_details_tbl")


read_df.to_sql('your_table_name', sqlalchemy_engine, if_exists='replace', index=False)

print("Data inserted successfully!")



