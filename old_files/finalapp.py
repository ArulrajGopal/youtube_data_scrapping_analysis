import streamlit as st
import sqlite3


# st.write("""
# ## my first app
#          """)


conn = sqlite3.connect('youtubedata.db')
cur = conn.cursor()

query1 = """select 
                Channel_name, 
                videos 
            from 
                channel_details_tbl
            where 
                videos = (select max(videos) from channel_details_tbl)"""


cur.execute(query1)
output = cur.fetchall()

conn.close()

print(output)