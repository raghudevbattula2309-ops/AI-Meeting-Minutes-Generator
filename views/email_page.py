"""
Email Page
"""

import streamlit as st
import streamlit.components.v1 as components

def render_email_page():

    st.header("📧 Follow-up Email")

    st.caption(
        "Review and edit the AI-generated email before sending."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Back",
            use_container_width=True
        ):

            st.session_state["page"] = "minutes"

            st.rerun()

    with col2:

     components.html(
        f"""
        <button
            onclick="copyEmail()"
            style="
                width:100%;
                height:38px;
                border-radius:8px;
                border:1px solid #d3d3d3;
                background:white;
                cursor:pointer;
                font-size:14px;">
            📋 Copy
        </button>

        <script>
        function copyEmail() {{
            navigator.clipboard.writeText(`{st.session_state["email"]}`);
            alert("Email copied to clipboard!");
        }}
        </script>
        """,
        height=45,
    )

    st.divider()

    st.text_area(
        "Email",
        key="email",
        height=500
    )