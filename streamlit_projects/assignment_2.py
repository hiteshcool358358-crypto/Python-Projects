import streamlit as st
import datetime as dt

st.title("Age Calculator")
st.subheader("You will be entering your date of birth and the program will calculate your age.")
st.write("Enter your date of birth:")
dob = st.date_input("Your dob here in (YYYY-MM-DD) format", dt.date(2000, 1, 1))

age = 2026 - dob.year
st.write(f"Your age is: {age} years")