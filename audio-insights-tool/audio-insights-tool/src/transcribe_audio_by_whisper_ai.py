import streamlit as st
from src.openai.open_ai import OpenAI


@st.cache_data(show_spinner=False, ttl=600, persist=None)
def transcribe_audio(audio_file):
    try:
        transcription = OpenAI().create_audio_model(
            file=audio_file,
            model="whisper-1",
            response_format="text"
        )
        return transcription
    except Exception as exp:
        st.error(exp)
