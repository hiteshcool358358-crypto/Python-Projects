import streamlit as st
import requests

st.title("Live Currency Converter")

with st.expander("Expand for help"):
    st.markdown("""
                - You need to enter your own currency in the sidebar
                - You should be connected to an internet or ethernet connection
                - If it doesn't work, try using it with a vpn""")
with st.sidebar:
    st.markdown("# Select Your Currency")
    def_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "GBP", "Euro", "Pakistani Rupee"])

    if def_curr == "":
        pass
    elif def_curr == "":
        pass
    elif def_curr == "":
        pass
    elif def_curr == "":
        pass
    elif def_curr == "":
        pass
    elif def_curr == "":
        pass

def_amt = st.number_input("Enter the amount for conversion:", min_value=0.00)
conv_curr = st.selectbox("Enter the currency in which you want to enter the amount of conversion:", ["United States Dollar", "Indian Rupee", "Japanese Yen", "GBP", "Euro", "Pakistani Rupee"])

if st.button("Convert"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][conv_curr]
        amt = def_amt * rate
        st.success("Conversion successful")
        st.write(f"{def_amt:.2f} {def_curr} = {amt:.2f} {conv_curr}")
    else:
        st.error("Conversion Failed!")