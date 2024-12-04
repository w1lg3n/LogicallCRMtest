import streamlit as st
from src.openai.open_ai import OpenAI

PROMPT = """
As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the provided phone sales transcript. Consider the following factors:
    1. Overall Tone: Assess the general mood or attitude conveyed during the conversation.
    2. Emotion in Language: Analyze the emotions expressed through specific words or phrases.
    3. Context: Evaluate the context in which these words and phrases are used to determine the emotional intent.

    Based on these factors, indicate whether the sentiment is **happy**, **upset**, or **normal**, and provide a brief explanation for your conclusion.

    Output in the following JSON format:
    {
        "sentiment": "<happy, upset, or normal>",
        "explanation": "<brief explanation of the sentiment>"
    }
    """


@st.cache_data(show_spinner=False, ttl=600, persist=None)
def sentiment_analysis(transcript):
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