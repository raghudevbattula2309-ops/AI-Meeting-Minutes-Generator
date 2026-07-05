"""
Meeting Minutes Page
"""

import streamlit as st

from services.word_export import export_minutes_to_word
from ai_service import generate_followup_email


def render_minutes_page():
    """
    Render Meeting Minutes Page.
    """

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    st.header("📝 Meeting Minutes")

    st.caption(
        "AI-generated meeting minutes from your transcript."
    )

    st.divider()

    # --------------------------------------------------
    # Toolbar
    # --------------------------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        if st.button(
            "⬅ Back",
            use_container_width=True
        ):

            st.session_state["page"] = "transcript"

            st.rerun()




    with col2:

        if not st.session_state["edit_mode"]:
              
            if st.button(
                "✏️ Edit",
                use_container_width=True
            ):
                st.session_state["edit_mode"] = True
                st.rerun()                        
        else:
               
            if st.button(
                "💾 Save",
                use_container_width=True
            ):
                st.session_state["minutes"] = st.session_state["minutes_editor"]

                st.session_state["edit_mode"] = False

                st.rerun()



    with col3:

        if st.button(
             "📄 Export",
        use_container_width=True
        ):
            word_file = export_minutes_to_word(
            st.session_state["minutes"]
            )
        
            st.download_button(
            label="⬇ Download Word Document",
            data=word_file,
            file_name="Meeting_Minutes.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
            )

    with col4:

        st.button(
            "📧 Email",
            use_container_width=True,
            disabled=False
        )

    with col5:

        st.button(
            "📋 Copy",
            use_container_width=True,
            disabled=True
        )

    st.divider()

    # --------------------------------------------------
    # Meeting Minutes
    # --------------------------------------------------

    st.success("✅ Meeting Minutes Generated Successfully!")

    if st.session_state["edit_mode"]:
       
       edited_minutes = st.text_area(
      "Edit Meeting Minutes",
      value=st.session_state["minutes"],
      height=600,
      key="minutes_editor"
      )
    
       st.session_state["minutes"] = edited_minutes

    else:

       st.markdown(st.session_state["minutes"])
       st.divider()

    # --------------------------------------------------
    # Generate Email
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

    if st.session_state["email"] != "":

        st.subheader("📧 Follow-up Email")

        st.markdown(st.session_state["email"])