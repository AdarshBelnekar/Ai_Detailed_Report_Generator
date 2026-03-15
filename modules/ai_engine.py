from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ddr(inspection_text, thermal_text):

    combined_data = f"""
INSPECTION REPORT
-----------------
{inspection_text}

THERMAL REPORT
--------------
{thermal_text}
"""

    prompt = f"""
You are a professional building diagnostics consultant.

Create a Detailed Diagnostic Report using the following structure.

Rules:
- Do NOT invent facts
- If information missing → write "Not Available"
- If there are conflicting observations → mention the conflict
- Use simple client-friendly language

Structure:

1 Executive Summary

2 Property Issue Overview
(Table with Issue Category, Location, Severity, Confidence)

3 Area-Wise Observations
Include:
- Visual Findings
- Thermal Findings
- Evidence Images
- Diagnostic Interpretation
- Severity Score
- Confidence Level

4 Probable Root Cause Analysis

5 Severity Assessment Framework

6 Recommended Remediation Actions
Immediate Actions
Preventive Actions
Follow-Up Inspection

7 Additional Observations

8 Missing or Unclear Information

9 AI Analysis Confidence

DATA:
{combined_data}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content