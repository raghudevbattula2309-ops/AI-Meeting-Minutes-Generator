"""
Header Component
"""

import streamlit as st


def render_header():
    """
    Renders the application header.
    """

    st.markdown(
        """
        <div style="text-align:center;">

        <h1>🤖 AI Engineering Meeting Assistant</h1>

        <p style="font-size:18px;color:gray;">
            AI-powered Meeting Minutes & Follow-up Email Generator
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align:center;">

        <p style="font-size:18px;">
            Automatically convert engineering meeting transcripts into:
        </p>

        <p style="font-size:22px;">
            📄 Executive Summary &nbsp;&nbsp;
            ✅ Action Items &nbsp;&nbsp;
            ⚠️ Risks &nbsp;&nbsp;
            🎯 Decisions &nbsp;&nbsp;
            📅 Next Steps
        </p>

        <hr>

        </div>
        """,
        unsafe_allow_html=True
    )