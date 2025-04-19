
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Learning Assistant", layout="centered")
st.title("AI Learning Assistant")

st.header("Define Your Learning Goals")
topic = st.text_input("Enter the topic you want to learn about:")
learning_goals = st.text_input("What are your learning objectives? (e.g., Understand basics, become proficient, etc.)")

st.header("Personalization")
interest_area = st.text_input("What is your main area of interest within this topic?")
knowledge_level = st.selectbox("What is your current knowledge level?", ["Beginner", "Intermediate", "Advanced"])
learning_style = st.selectbox("Preferred learning style", ["Visual", "Text", "Summarize","Examples"])

if st.button("Generate Report"):
    st.session_state['user_profile'] = {
        "Topic": topic,
        "Goals": learning_goals,
        "Interest Area": interest_area,
        "Knowledge Level": knowledge_level,
        "Learning Style": learning_style
    }
    st.switch_page("pages/report_page.py")
 

