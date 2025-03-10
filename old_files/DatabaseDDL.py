import sqlite3

conn = sqlite3.connect('youtubedata.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS channel_details_tbl
            (Channel_name TEXT,
            Subscribers INT,
            views INT,
            videos INT,
            upload_plylst_id TEXT
            )''')


conn.commit()
conn.close()