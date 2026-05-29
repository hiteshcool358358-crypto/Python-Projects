import streamlit as st

st.markdown("## Welcome to Jharkhand Elections 2026")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Seal_of_Jharkhand.svg/960px-Seal_of_Jharkhand.svg.png", width=200)
col1, col2, col3, col4 = st.columns(4)

if "VoteBJP" not in st.session_state:
    st.session_state.VoteBJP = 0
if "VoteINC" not in st.session_state:
    st.session_state.VoteINC = 0
if "VoteJMM" not in st.session_state:
    st.session_state.VoteJMM = 0
if "VoteNOTA" not in st.session_state:
    st.session_state.VoteNOTA = 0

with col1:
    st.header("BJP")
    st.subheader("Batenge Toh Katenge!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Actual_BJP_Flag.svg/500px-Actual_BJP_Flag.svg.png", width=150)
    st.write("We will provide:\n1. Free electricity\n2. Religious harmony\n3. Anti-corruption measures")
    button1 = st.button("Vote for BJP")
    if button1:
        st.session_state.VoteBJP += 1
with col2:
    st.header("INC")
    st.subheader("Congress ka Haath, Aam Aadmi ke Saath!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/INC_Flag_Official.jpg", width=150)
    st.write("We will provide:\n1. Free electricity\n2. Religious harmony\n3. Anti-corruption measures")
    button2 = st.button("Vote for INC")
    if button2:
       st.session_state.VoteINC += 1
with col3:
    st.header("JMM")
    st.subheader("Jai Jharkhand!")
    st.image("data:image/png;base64,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", width=150)
    st.write("We will provide:\n1. Free electricity\n2. Religious harmony\n3. Anti-corruption measures")
    button3 = st.button("Vote for JMM")
    if button3:
        st.session_state.VoteJMM += 1
with col4:
    st.header("NOTA")
    st.subheader("None of the Above!")
    st.image("data:image/png;base64,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", width=150)
    button4 = st.button("Vote for NOTA")
    if button4:
        st.session_state.VoteNOTA += 1

if button1:
    st.success("Thank you for voting for BJP! It has been registered successfully.")
elif button2:
    st.success("Thank you for voting for INC! It has been registered successfully.")
elif button3:
    st.success("Thank you for voting for JMM! It has been registered successfully.")
elif button4:
    st.success("Thank you for voting for NOTA! It has been registered successfully but it won't do anything. LOL you absolute moron! 🤡🤡🤣🤣")

st.markdown("## Live Election Counting")
st.write(f"BJP: {st.session_state.VoteBJP} votes")
st.write(f"INC: {st.session_state.VoteINC} votes")
st.write(f"JMM: {st.session_state.VoteJMM} votes")
st.write(f"NOTA: {st.session_state.VoteNOTA} votes")

declaration = st.button("Declare Results (To be pressed only by the booth administrator)")
if declaration:
    if st.session_state.VoteBJP > st.session_state.VoteINC and st.session_state.VoteBJP > st.session_state.VoteJMM and st.session_state.VoteBJP > st.session_state.VoteNOTA:
        st.success("BJP wins the election!")
        st.markdown("# Elections closed! No more votes will be accepted.")
        st.markdown("Thank you for participating in the democratic process. See you in the next election!")
    elif st.session_state.VoteINC > st.session_state.VoteBJP and st.session_state.VoteINC > st.session_state.VoteJMM and st.session_state.VoteINC > st.session_state.VoteNOTA:
        st.success("INC wins the election!")   
        st.markdown("# Elections closed! No more votes will be accepted.")
        st.markdown("Thank you for participating in the democratic process. See you in the next election!")
    elif st.session_state.VoteJMM > st.session_state.VoteBJP and st.session_state.VoteJMM > st.session_state.VoteINC and st.session_state.VoteJMM > st.session_state.VoteNOTA:
        st.success("JMM wins the election!")
        st.markdown("# Elections closed! No more votes will be accepted.")
        st.markdown("Thank you for participating in the democratic process. See you in the next election!")
    elif st.session_state.VoteNOTA > st.session_state.VoteBJP and st.session_state.VoteNOTA > st.session_state.VoteINC and st.session_state.VoteNOTA > st.session_state.VoteJMM:
        st.warning("The election is won by NOTA but nothing happens. LOL you absolute morons! 🤡🤡🤣🤣")
        st.markdown("# Elections closed! No more votes will be accepted.")
        st.markdown("Thank you for participating in the democratic process. See you in the next election!")
    else:
        st.error("The elections were cancelled due to some reasons. Will be held after further notification and notice.")
        st.markdown("# Elections closed! No more votes will be accepted.")
        st.markdown("Thank you for participating in the democratic process. See you in the next election!")