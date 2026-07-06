"""
AI Engineering Meeting Assistant

Main Application
"""

import streamlit as st
from views.email_page import render_email_page
from utils.session import initialize_session
from components.header import render_header
from views.transcript_page import render_transcript_page
from views.minutes_page import render_minutes_page


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="AI Engineering Meeting Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# Initialize Session
# ==================================================

initialize_session()


# ==================================================
# Main Application.03
# ==================================================

def main():

    render_header()

    if st.session_state["page"] == "transcript":

        render_transcript_page()

    elif st.session_state["page"] == "minutes":

        render_minutes_page()

    elif st.session_state["page"] == "email":

        render_email_page()


# ==================================================
# Entry Point
# ==================================================

if __name__ == "__main__":
    main()