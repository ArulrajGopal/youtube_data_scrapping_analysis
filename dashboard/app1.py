import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.title("My First Streamlit App 🚀")

# Add text
st.write("Welcome to this simple Streamlit app!")

# User input
name = st.text_input("Enter your name:")
age = st.slider("Select your age", 1, 100, 25)

if name:
    st.success(f"Hello, {name}! You are {age} years old.")

# Generate sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Show data table
st.subheader("Sample Data")
st.dataframe(data)

# Line chart
st.subheader("Line Chart")
st.line_chart(data)

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(data)

# Checkbox example
if st.checkbox("Show Raw Data"):
    st.write(data)
