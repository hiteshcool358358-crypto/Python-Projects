import streamlit as st

st.title("Daily MIS Report")

date = st.date_input("Enter the date of the entry here")
shift = st.selectbox("Enter entry's shift here", ["A", "B", "C", "G", "N"])
part = st.text_input("Enter part no. here")
proc = st.selectbox("Enter process here", ["ASSY", "PAINTING", "CED", "STRESS PEENNING", "SHORT PEENING", "TEMPERING", "HEAT TREATMENT", "SHEARING", "PARABOLIC", "DRILLING - MANUAL", "SPM DRILLING", "HOT PUNCHING", "COLD PUNCHING", "WRAPPER FORMING", "EYE FORMING", "TAPER ROLLING", "V - CUTTING", "BENDING", "NIBBING", "STRAIGHT CUTTING", "BUSH PRESS", "SCARGING", "MATCHING", "MILLING", "OTHERS"])
defect = st.selectbox("Enter defect here", ["CAMBER HIGH", "CAMBER DOWN", "EYE CRACK", "MELT", "BROKEN", "BEND", "HARDNESS LOW", "HARDNESS HIGH", "HOLE OUT - WIDTHWISE", "HOLE OUT - LENGTHWISE", "LENGTH UNDERSIZE", "OTHERS"])
obs = st.text_input("Enter your actual observation here")
qty = st.number_input("Enter qty. here")
op = st.text_input("Enter operator's name here")
ins = st.text_input("Enter inspector's name here")
stat = st.text_input("Enter rework/rejection status here")

if st.button("Register info."):
    with open("MIS Report.csv", "a") as f:
        f.write(f"\n{date},{shift},{part},{proc},{defect},{obs},{qty},{op},{ins},{stat}")