import streamlit as st

#Welcoming the voters to the election system
st.markdown("## Welcome to Jharkhand Elections 2026")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Seal_of_Jharkhand.svg/960px-Seal_of_Jharkhand.svg.png", width=200)
col1, col2, col3, col4 = st.columns(4)

#Initializing the vote counts for each party and NOTA in the session state
if "VoteBJP" not in st.session_state:
    st.session_state.VoteBJP = 0
if "VoteINC" not in st.session_state:
    st.session_state.VoteINC = 0
if "VoteJMM" not in st.session_state:
    st.session_state.VoteJMM = 0
if "VoteNOTA" not in st.session_state:
    st.session_state.VoteNOTA = 0

#Displaying the parties and NOTA options for voting
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Jharkhand_Mukti_Morcha_logo.svg/500px-Jharkhand_Mukti_Morcha_logo.svg.png", width=150)
    st.write("We will provide:\n1. Free electricity\n2. Religious harmony\n3. Anti-corruption measures")
    button3 = st.button("Vote for JMM")
    if button3:
        st.session_state.VoteJMM += 1
with col4:
    st.header("NOTA")
    st.subheader("None of the Above!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/NOTA_Option_Logo.svg/500px-NOTA_Option_Logo.svg.png", width=150)
    button4 = st.button("Vote for NOTA")
    if button4:
        st.session_state.VoteNOTA += 1

#Displaying the success message after voting for any party or NOTA
if button1:
    st.success("Thank you for voting for BJP! It has been registered successfully.")
elif button2:
    st.success("Thank you for voting for INC! It has been registered successfully.")
elif button3:
    st.success("Thank you for voting for JMM! It has been registered successfully.")
elif button4:
    st.success("Thank you for voting for NOTA! It has been registered successfully but it won't do anything. LOL you absolute moron! 🤡🤡🤣🤣")

#Displaying the live election counting and the declaration button for the booth administrator
st.markdown("## Live Election Counting")
st.write(f"BJP: {st.session_state.VoteBJP} votes")
st.write(f"INC: {st.session_state.VoteINC} votes")
st.write(f"JMM: {st.session_state.VoteJMM} votes")
st.write(f"NOTA: {st.session_state.VoteNOTA} votes")

#The booth administrator can declare the results by pressing the declaration button. The results will be declared based on the highest votes received by any party or NOTA. If there is a tie or if NOTA wins, appropriate messages will be displayed.
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

#The app have been deployed. In order to use it click on this link: https://python-projects-kukvr9uubwsjsnmizdfqz5.streamlit.app/