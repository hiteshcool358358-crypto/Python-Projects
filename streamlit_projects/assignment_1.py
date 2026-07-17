import streamlit as st

st.title("Welcome to my first python web app")
st.subheader("This is a language picker.")
st.text("You will be selecting your fav. programmin lang. from the dropdown below.")
st.write("Select your fav. programming language:")
lang = st.selectbox("Programming Language", ["Python", "Java", "HTML", "C++", "CSS", "JS"])
st.write(f"What a choice! Your fav, programming language is {lang}")