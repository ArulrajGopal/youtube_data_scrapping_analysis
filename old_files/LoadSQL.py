
import pandas as pd
import sqlite3
from MongoConfiguration import *

read_mongo_db = client.YoutubeScrapping
channel_details_df = pd.DataFrame(read_mongo_db .channel_details.find({},{'_id': False}))


conn = sqlite3.connect('youtubedata.db')
cur = conn.cursor()

#loading channel_details_tbl
for row in channel_details_df.itertuples():
    insert_sql = f"INSERT INTO channel_details_tbl values ('{row[1]}',{row[2]},{row[3]},{row[4]},'{row[5]}')"
    cur.execute(insert_sql)


conn.commit()
conn.close()


