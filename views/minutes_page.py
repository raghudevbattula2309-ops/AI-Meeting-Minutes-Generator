"""
Meeting Minutes Page
"""

import streamlit as st

from ai_service import generate_followup_email


def render_minutes_page():
    """
    Render Meeting Minutes Page.
    """

    # --------------------------------------------------
    # Back Button
    # --------------------------------------------------

    if st.button("⬅ Back to Transcript"):

        st.session_state["page"] = "transcript"

        st.rerun()

    st.divider()

    # --------------------------------------------------
    # Meeting Minutes
    # --------------------------------------------------

    st.success("✅ Meeting Minutes Generated Successfully!")

    st.markdown(st.session_state["minutes"])

    st.divider()

    # --------------------------------------------------
    # Generate Follow-up Email
    # --------------------------------------------------

    if st.button(
        "📧 Generate Follow-up Email",
        use_container_width=True
    ):

        with st.spinner(
            "📧 Generating professional email..."
        ):

            email = generate_followup_email(
                st.session_state["minutes"]
            )

        st.session_state["email"] = email

    # --------------------------------------------------
    # Display Email
    # --------------------------------------------------

    if st.session_state.get("email", "") != "":

        st.subheader("📧 Follow-up Email")

        st.markdown(st.session_state["email"])