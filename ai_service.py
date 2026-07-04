"""
AI Service Layer

Responsible for communicating with Google's Gemini AI.
"""

import truststore
truststore.inject_into_ssl()

import os
from google import genai
from dotenv import load_dotenv

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# Gemini Configuration
# --------------------------------------------------

MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(api_key=API_KEY)


# --------------------------------------------------
# Generate Meeting Minutes
# --------------------------------------------------

def generate_meeting_minutes(transcript):

    prompt = f"""
You are a Senior Engineering Project Manager working in an Aerospace company.

Analyze the Microsoft Teams meeting transcript below.

Generate professional meeting minutes using EXACTLY the following structure.

# 📄 Executive Summary

Provide a concise executive summary.

---

# ✅ Action Items

Create a markdown table.

| Owner | Action | Due Date |

If no due date exists write "Not Specified".

---

# ⚠ Risks

List all project risks.

---

# 🎯 Decisions

List all decisions made.

---

# 📅 Next Steps

List the next activities.

---

# 📝 Overall Project Status

Choose ONLY ONE

🟢 On Track

🟡 Needs Attention

🔴 Critical

---

Finally provide recommendations for the Project Manager.

IMPORTANT RULES

This application is used for Engineering Project Meetings.

Strictly follow these rules:

1. Use ONLY information explicitly present in the transcript.
2. Never invent or assume:
   - Dates
   - Times
   - Names
   - Roles
   - Project names
   - Risks
   - Decisions
   - Action items
   - Due dates
3. If information is not mentioned, write "Not Specified".
4. Do not fabricate examples.
5. Do not add generic recommendations unrelated to the transcript.
6. Keep the language professional and suitable for executive review.

Meeting Transcript:

{transcript}
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
## ❌ Error

Unable to generate meeting minutes.

Reason:

{str(e)}
"""


# --------------------------------------------------
# Generate Follow-up Email
# --------------------------------------------------

def generate_followup_email(meeting_minutes):

    prompt = f"""
You are a Senior Engineering Project Manager.

Generate a professional Outlook follow-up email.

Include:

- Subject
- Greeting
- Meeting Summary
- Action Items
- Closing

Meeting Minutes

{meeting_minutes}
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
## ❌ Error

Unable to generate follow-up email.

Reason:

{str(e)}
"""