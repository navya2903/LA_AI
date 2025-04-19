import streamlit as st

def get_user_profile(topic, goals):
    interest_area = st.text_input(f"What specific subtopics or aspects of {topic} are you most interested in?")
    knowledge_level = st.selectbox("What is your current knowledge level?", ["", "Beginner", "Intermediate", "Advanced"])
    learning_style = st.selectbox("Preferred learning format?", ["", "Text", "Visuals", "Examples", "Summaries"])

    return {
        "Topic": topic,
        "Goals": goals,
        "Interest Area": interest_area,
        "Knowledge Level": knowledge_level,
        "Learning Style": learning_style
    }
