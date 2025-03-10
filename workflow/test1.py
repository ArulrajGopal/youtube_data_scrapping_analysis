from integrate_utils import *
from config import *    

df = fetch_dynamo_data_into_pd_dataframe("channel_details_tbl")

import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
}
df = pd.DataFrame(data)

# PostgreSQL Connection Details
user = 'your_username'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'your_database'

# Create SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# Write DataFrame to PostgreSQL table
df.to_sql('your_table_name', engine, if_exists='replace', index=False)

print("Data inserted successfully!")

