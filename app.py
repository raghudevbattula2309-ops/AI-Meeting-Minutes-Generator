"""
AI Engineering Meeting Assistant

Main Application
"""

import streamlit as st

from utils.session import initialize_session
from components.header import render_header
from pages.transcript_page import render_transcript_page
from pages.minutes_page import render_minutes_page


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
# Main Application
# ==================================================

def main():

    render_header()

    if st.session_state["page"] == "transcript":

        render_transcript_page()

    else:

        render_minutes_page()


# ==================================================
# Entry Point
# ==================================================

if __name__ == "__main__":
    main()