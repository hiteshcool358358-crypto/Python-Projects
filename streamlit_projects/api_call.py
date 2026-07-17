import streamlit as st
import requests

st.title("Currency Converter")
amt_inr = st.number_input("Enter the amount in INR", min_value=1.0)

curr = st.selectbox("Conver to: ", ["USD", "EUR", "JPY", "GBP"])
comm = st.button("Convert")

if comm:
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][curr]
        new_amt = float(amt_inr) * rate
        st.write(f"Converted amount in {curr}: {new_amt:.2f}")
    else:
        st.error("Failed to convert")