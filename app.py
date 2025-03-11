# streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("🚀 Welcome to Your Growth Journey !")
st.write("Embrace challenges, This AI-powered app helps you build a growth mindset challenges,and achievements!")

# quit section
st.header("💡 Todays Growth Mindset Qoute")
st.write("Succeess is not final, failiure is not fatal: it is the courage to continue that counts.")

st.header("🔧 Whats Your Challenge Today")
user_input = st.text_input("Describe a challenge you are facing:")


# condition
if user_input:
    st.success(f" you re facing: {user_input}. keep pushing forword towards your goal!")
else:
    st.warning("Tell us about yor challenge to get started!")

#reflexing
st.header(" Reflect on Your Learning")
reflection = st.text_area("Write your reflections here")

if reflection:
    st.success(f" Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past! Share your difficulties")

#achievements
st.header("Celbrate Your Wins!")
acheivement = st.text_input("Share something you ve recently accomplished:")


if acheivement:
    st.success(f"Amazing! You achieved: {acheivement}")
else:
    st.info("Big or small , every acheivement counts! Share one now")

#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ✨")
st.write("🧧 Created by Shamshad Shah")

