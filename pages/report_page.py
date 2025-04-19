import streamlit as st
from report import generate_report, draw_sample_chart
from research import simulate_research

st.set_page_config(page_title="Your Learning Report", layout="centered")
st.title("Your Personalized Learning Report")

if 'user_profile' in st.session_state:
    user_profile = st.session_state['user_profile']
    research_data = simulate_research(user_profile['Topic'])

    report_md = generate_report(user_profile, research_data)
    st.markdown(report_md, unsafe_allow_html=True)
    st.pyplot(draw_sample_chart(user_profile['Topic']))

    st.subheader("Have Questions or Feedback?")
    followup = st.text_area("Ask a follow-up question or provide feedback:")

    if st.button("Update Report"):
        updated_response = f"*Based on your input:* **{followup}**, here’s an updated insight:\n\n" \
                           f"We suggest further exploring subtopics or adjusting learning resources accordingly. Thankyou."

        st.markdown("---")
        st.subheader("Updated Report Suggestion")
        st.markdown(updated_response, unsafe_allow_html=True)
else:
    st.warning("Please fill in your details on the home page first.")
    st.page_link("app.py", label="Go to Home")
