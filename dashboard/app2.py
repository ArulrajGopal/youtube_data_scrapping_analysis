# pip install streamlit psycopg2 sqlalchemy pandas

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page title
st.title("PostgreSQL Data Viewer")

# Database connection parameters
host = "localhost"         # change to your server
port = "5432"              # default port for PostgreSQL
database = "postgres"       # your database name
user = "postgres"          # your username
password = "Arulraj_1234" # your password

# Create database connection
def get_connection():
    try:
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
        return engine
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Fetch data from database
def get_data():
    engine = get_connection()
    if engine:
        query = "select title, videocount, viewcount from channel_details_stage;"  # Replace with your table name
        try:
            df = pd.read_sql(query, engine)
            return df
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return pd.DataFrame()
    return pd.DataFrame()

# Display data in Streamlit
if st.button("Load Data"):
    df = get_data()
    if not df.empty:
        st.success("Data loaded successfully!")
        st.dataframe(df)
        st.subheader("Line Chart")
        st.line_chart(df)
    else:
        st.warning("No data found or unable to fetch data.")




