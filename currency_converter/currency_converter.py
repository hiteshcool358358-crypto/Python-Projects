import streamlit as st
import requests

st.title("Live Currency Converter")

with st.expander("Expand for help"):
    st.markdown("""
                ##### Guide:
                - You need to enter your own currency in the sidebar
                - You should be connected to an internet or ethernet connection
                - If it doesn't work, try using it with a vpn
                """)
with st.sidebar:
    st.markdown("# Select Your Currency")
    def_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "Great British Pound", "Euro", "Pakistani Rupee"])

    if def_curr == "United States Dollar":
        short_curr = "USD"
        url = "https://api.exchangerate-api.com/v4/latest/USD"
    elif def_curr == "Indian Rupee":
        short_curr = "INR"
        url = "https://api.exchangerate-api.com/v4/latest/INR"
    elif def_curr == "Japanese Yen":
        short_curr = "JPY"
        url = "https://api.exchangerate-api.com/v4/latest/JPY"
    elif def_curr == "Great British Pound":
        short_curr = "GBP"
        url = "https://api.exchangerate-api.com/v4/latest/GBP"
    elif def_curr == "Euro":
        short_curr = "EUR"
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
    elif def_curr == "Pakistani Rupee":
        short_curr = "PKR"
        url = "https://api.exchangerate-api.com/v4/latest/PKR"

def_amt = st.number_input("Enter the amount for conversion:", min_value=0.00)
conv_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "Great British Pound", "Euro", "Pakistani Rupee"])

if conv_curr == "United States Dollar":
    new_curr = "USD"   
elif conv_curr == "Indian Rupee":
    new_curr = "INR"  
elif conv_curr == "Japanese Yen":
    new_curr = "JPY"
elif conv_curr == "Great British Pound":
    new_curr = "GBP"
elif conv_curr == "Euro":
    new_curr = "EUR"
elif conv_curr == "Pakistani Rupee":
    new_curr = "PKR"

if st.button("Convert"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][new_curr]
        amt = def_amt * rate
        st.success("Conversion successful")
        st.write(f"{def_amt:.2f} {short_curr} = {amt:.2f} {new_curr}")
    else:
        st.error("Conversion Failed!")