import streamlit as st
import pandas as pd

st.title("Upload file:")

json_file = st.file_uploader("Upload your json file here:", type=["json"])
if json_file:
    df = pd.read_json(json_file)
    st.dataframe(df)

csv_file = st.file_uploader("Upload your csv file here:", type=["csv"])
if csv_file:
    df = pd.read_csv(csv_file)
    st.dataframe(df)
    st.write(df.describe())
    value = df["Pulse"].unique()
    selected_values = st.selectbox("Filter by pulse values", value)
    filtered_data = df[df["Pulse"] == selected_values]
    st.dataframe(filtered_data)
    st.write(filtered_data.describe())