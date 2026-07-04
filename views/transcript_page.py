"""
Transcript Page

Handles:
- Transcript input
- Upload transcript
- Import latest transcript
- Clear transcript
- Statistics
- Generate meeting minutes
"""

from pathlib import Path

import streamlit as st
from docx import Document

from ai_service import generate_meeting_minutes


def render_transcript_page():
    """
    Render Transcript Page.
    """

    # --------------------------------------------------
    # Transcript Input
    # --------------------------------------------------

    meeting_text = st.text_area(
        "📋 Paste your Microsoft Teams meeting transcript",
        value=st.session_state["meeting_text"],
        height=300,
        placeholder="Paste your meeting transcript here..."
    )

    st.session_state["meeting_text"] = meeting_text

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.caption(
            f"Characters: {len(st.session_state['meeting_text'])}"
        )

    with col2:
        st.caption(
            f"Words: {len(st.session_state['meeting_text'].split())}"
        )

    # --------------------------------------------------
    # Upload Transcript
    # --------------------------------------------------

    uploaded_file = st.file_uploader(
        "📄 Upload Transcript (.txt or .docx)",
        type=["txt", "docx"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".txt"):

            st.session_state["meeting_text"] = (
                uploaded_file.read().decode("utf-8")
            )

        elif uploaded_file.name.endswith(".docx"):

            document = Document(uploaded_file)

            st.session_state["meeting_text"] = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        st.rerun()

    # --------------------------------------------------
    # Action Buttons
    # --------------------------------------------------

    col1, col2, col3 = st.columns([2, 1, 4])

    with col1:

        import_latest = st.button(
            "📂 Import Latest Transcript",
            use_container_width=True
        )

    with col2:

        clear_text = st.button(
            "🗑 Clear",
            use_container_width=True
        )

    # --------------------------------------------------
    # Import Latest
    # --------------------------------------------------

    if import_latest:

        transcript_path = Path.home() / "Downloads" / "meeting.txt"

        if transcript_path.exists():

            st.session_state["meeting_text"] = transcript_path.read_text(
                encoding="utf-8"
            )

            st.success("✅ Transcript imported successfully!")

            st.rerun()

        else:

            st.error("❌ meeting.txt not found in Downloads folder.")

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    if clear_text:

        st.session_state["meeting_text"] = ""
        st.session_state["minutes"] = ""

        st.rerun()

    st.divider()

    # --------------------------------------------------
    # Generate Meeting Minutes
    # --------------------------------------------------

    if st.button(
        "🚀 Generate Meeting Minutes",
        use_container_width=True
    ):

        if st.session_state["meeting_text"].strip() == "":

            st.warning(
                "Please paste or upload a meeting transcript."
            )

        else:

            with st.spinner(
                "🤖 AI is analyzing the meeting..."
            ):

                result = generate_meeting_minutes(
                    st.session_state["meeting_text"]
                )

            st.session_state["minutes"] = result

            st.session_state["page"] = "minutes"

            st.rerun()