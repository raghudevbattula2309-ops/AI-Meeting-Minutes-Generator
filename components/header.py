"""
Header Component
"""

import streamlit as st


def render_header():
    """
    Renders the application header.
    """

    st.title("🤖 AI Engineering Meeting Assistant")

    st.markdown("""
Automatically convert engineering meeting transcripts into:

📄 Executive Summary  ✅ Action Items  ⚠️ Risks  🎯 Decisions  📅 Next Steps

---
""")