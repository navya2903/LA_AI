
import streamlit as st
import matplotlib.pyplot as plt
import random

def draw_sample_chart(topic):
    labels = ['Core Concepts', 'Applications', 'Challenges', 'Trends']
    values = [random.randint(20, 40) for _ in labels]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color='skyblue')
    ax.set_title(f'{topic} Breakdown')
    ax.set_ylabel("Importance Level")
    return fig

def generate_report(user_profile, research_data):
    report = f"""Educational Report: {user_profile['Topic']}

### Objectives
{user_profile['Goals']}

### Focus Area
Main interest: **{user_profile['Interest Area']}**  
Level: **{user_profile['Knowledge Level']}**

### Research Summary
- **Web**: {research_data['web']}
- **Academic**: {research_data['academic']}
- **Video**: {research_data['video']}

### Recommended Approach
Since you prefer **{user_profile['Learning Style']}**, we suggest:
- Structured notes with visuals
- Use of real-world examples
- Recap summaries for revision
"""

   
    style = user_profile['Learning Style'].lower()

    if style == "text":
        report += f"""

### In-Depth Explanation
Here's a deeper dive into **{user_profile['Topic']}** and its key aspects:
- Definitions and core concepts
- Important theories or models
- Related fields and applications
"""

    elif style == "visuals":
        st.pyplot(draw_sample_chart(user_profile['Topic']))

    elif style == "examples":
        report += f"""

### Examples
Here are some illustrative examples related to **{user_profile['Topic']}**:
- Example 1: Real-world application of the topic
- Example 2: Use in industry or research
- Example 3: Common pitfalls or challenges
"""

    elif style == "summaries":
        report += f"""

### Quick Summary
**{user_profile['Topic']}** is a key area involving **{user_profile['Interest Area']}**.
It’s vital to understand this for: _{user_profile['Goals'].lower()}_.
"""

    return report
