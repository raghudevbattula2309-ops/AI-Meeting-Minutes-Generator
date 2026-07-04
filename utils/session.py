"""
Session Management

Initializes all Streamlit Session State variables.
"""

import streamlit as st


def initialize_session():
    """
    Initialize all session state variables.
    """

    defaults = {

    "page": "transcript",

    "meeting_text": "",

    "minutes": "",

    "email": "",

    "edit_mode": False

}

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value