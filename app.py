from pathlib import Path
from docx import Document
import streamlit as st

from ai_service import (
    generate_meeting_minutes,
    generate_followup_email
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Engineering Meeting Assistant",
    layout="wide"
)

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

if "meeting_text" not in st.session_state:
    st.session_state["meeting_text"] = ""

if "minutes" not in st.session_state:
    st.session_state["minutes"] = ""

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🤖 AI Engineering Meeting Assistant")

st.markdown("""
Automatically convert engineering meeting transcripts into:

- 📄 Executive Summary
- ✅ Action Items
- ⚠️ Risks
- 🎯 Decisions
- 📅 Next Steps

---
""")

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

st.markdown("### OR")

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
# Transcript Actions
# --------------------------------------------------

col1, col2 = st.columns(2)

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
# Button Actions
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

if clear_text:

    st.session_state["meeting_text"] = ""
    st.session_state["minutes"] = ""

    st.rerun()

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
# Generate Meeting Minutes
# --------------------------------------------------

if st.button("🚀 Generate Meeting Minutes"):

    if st.session_state["meeting_text"].strip() == "":

        st.warning("Please paste or upload a meeting transcript.")

    else:

        with st.spinner("🤖 AI is analyzing the meeting..."):

            result = generate_meeting_minutes(
                st.session_state["meeting_text"]
            )
        st.write(result)
        st.session_state["minutes"] = result

# --------------------------------------------------
# Display Meeting Minutes
# --------------------------------------------------

if st.session_state["minutes"] != "":

    st.success("✅ Meeting Minutes Generated Successfully!")

    st.markdown(st.session_state["minutes"])

    st.markdown("---")

    # ----------------------------------------------
    # Generate Follow-up Email
    # ----------------------------------------------

    if st.button("📧 Generate Follow-up Email"):

        with st.spinner("📧 Generating professional email..."):

            email = generate_followup_email(
                st.session_state["minutes"]
            )

        st.subheader("📧 Follow-up Email")

        st.markdown(email)