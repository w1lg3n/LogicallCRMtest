import streamlit as st
from src.openai.open_ai import OpenAI

PROMPT = """
###Task Overview
    Your role as an AI is to analyze phone call transcripts to ensure they adhere to dietary supplement regulations and company policies. Your goal is to identify and report key compliance risks and extract relevant keywords from each compliance category mentioned in the transcripts.

### Steps:
    #### 1. Detect Key Phrases
        Extract key phrases from the transcripts that indicate potential compliance risks:
    
          1. Health Claims (Keywords: diagnose, treat, cure, prevent):
             - Identify statements that suggest a supplement can diagnose, treat, cure, or prevent diseases, e.g., "take this supplement to prevent cancer," "this product will treat."
    
          2. Unsubstantiated Claims (Keywords: guarantee, overnight):
             - Flag claims that exaggerate benefits without evidence or scientific backing, e.g., "guaranteed results," "works overnight."
    
          3. Misleading Statements (Keywords: proven, all-natural):
             - Spot misleading claims about product effects or ingredients, e.g., "clinically proven," "100% natural."
    
          4. False Guarantees (Keywords: loss, gain):
             - Detect unrealistic promises not supported by scientific evidence, e.g., "you will lose weight," "you will gain muscle."
    
          5. Exaggerated Testimonials:
             - Identify anecdotes or customer statements presented as definitive proof without proper disclaimers, e.g., "all customers say it works", "everyone who's tried it loves it."
    
          6. Non-Disclosure of Risks:
             - Note any omissions of potential side effects, interactions with medications, or other risks, e.g., "no side effects," "safe with any medication."
    
          7. Pressure Tactics:
             - Detect aggressive sales tactics or false urgency, e.g., "don't you want to feel better," "limited time offer."
    
          8. Off-Label Promotion:
             - Flag any promotion of supplements for unapproved uses, e.g., "also great for skin health," when not approved for such use.
    
          9. Regulatory References:
             - Ensure accurate references to regulatory bodies, e.g., "FDA approved," "complies with FDA regulations."

    #### 2. Color Coding
        Assign a color to each finding based on the urgency:
          - Blue: Immediate attention required.
          - Red: Keyword or phrase detected.
          - Orange: Review needed within 24-48 hours.

    #### 3. Output Format
        Structure the results in a JSON format displaying detected key phrases and their categories:
        {
            "Detected Key Phrases": {
                "Health Claims": [
                    {
                        "keyword": "<Keyword>",
                        "found": "<Exact or related term from the transcript>",
                        "color": "<Blue/Red/Orange>"
                    },
                    ...
                ],
                ...
            }
        }
"""


@st.cache_data(show_spinner=False, ttl=600, persist=None)
def searched_keywords(transcript):
    messages = [
        {
            "role": "system",
            "content": PROMPT
        },
        {
            "role": "user",
            "content": f"Transcript: {transcript}"
        }
    ]
    try:
        response = OpenAI().create_chat_model(
            model="gpt-4o-mini",
            temperature=0.18,
            messages=messages,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as exp:
        st.error(exp)
