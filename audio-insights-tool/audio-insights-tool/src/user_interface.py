import os
import json
import streamlit as st
from src.transcribe_audio_by_whisper_ai import transcribe_audio
from src.search_keywords_by_gpt import searched_keywords
from src.sentiment_analysis_by_gpt import sentiment_analysis


def get_api_key():
    """Fetch the OpenAI API key from user input."""
    api_key = st.text_input("Enter your OpenAI API key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    return api_key


def get_keywords_input():
    """Get keywords input from the user."""
    st.subheader("🔍 Keyword Search")
    keywords = st.text_input("Enter keywords or phrases to search (comma-separated)", "help, delay, upset")
    return keywords


def process_transcription(audio_file):
    """Handle transcription of the audio file."""
    st.subheader("📝 Transcription and Analysis")
    with st.spinner("Processing audio file..."):
        transcript = transcribe_audio(audio_file)  # Assuming this is a valid function for transcription
        if transcript:
            st.success("Transcription completed!")
            st.write("#### Transcription:")
            with st.expander("Click to show transcript", expanded=False):
                st.write(transcript)
        return transcript


def handle_keyword_search(transcript):
    """Perform keyword search in the transcript."""
    st.write("---")
    st.subheader("Keyword Search Results")

    with st.spinner("Searching for keywords in the transcript..."):
        found_keywords_list = json.loads(searched_keywords(transcript=transcript))
        cols = st.columns(3)
        for i, values in enumerate(found_keywords_list["Detected Key Phrases"].items()):
            with cols[i % 3]:
                with st.expander(values[0], expanded=False):
                    for value in values[1]:
                        st.write(f"Keyword: :{value['color'].lower()}[{value['keyword']}]")
                        st.write(f"Found: {value['found']}")


def display_sentiment(sentiment):
    """Display sentiment result with appropriate color."""
    if sentiment == "happy":
        st.write(f"The sentiment of this audio transcript is **:green[{sentiment}]**")
    elif sentiment == "upset":
        st.write(f"The sentiment of this audio transcript is **:red[{sentiment}]**")
    else:
        st.write(f"The sentiment of this audio transcript is **{sentiment}**")


def handle_sentiment_analysis(transcript):
    """Perform sentiment analysis on the transcript."""
    st.write("---")
    st.subheader("Sentiment Analysis")

    with st.spinner("Performing sentiment analysis..."):
        sentiment_result = json.loads(sentiment_analysis(transcript))
        sentiment = sentiment_result["sentiment"]
        explanation = sentiment_result["explanation"]

        st.write("#### Sentiment Analysis:")
        display_sentiment(sentiment)

        with st.expander("Sentiment Explanation", expanded=False):
            st.write(explanation)


def handle_audio_file(audio_file, max_file_size_mb):
    """Process the uploaded audio file, perform transcription, keyword search, and sentiment analysis."""
    file_size_mb = audio_file.size / (1024 * 1024)

    # File size validation
    if file_size_mb > max_file_size_mb:
        st.error(f"File size exceeds the {max_file_size_mb} MB limit. Your file is {file_size_mb:.2f} MB.")
    else:
        st.success(f"File size is {file_size_mb:.2f} MB, within the allowed limit.")
        st.audio(audio_file, format="audio/mpeg", loop=False)
        st.write("---")

        # Create columns for layout and display a button in the last column
        cols = st.columns(4)
        process_clicked = cols[-1].button("Process", use_container_width=True)

        # Check if the button was clicked
        if process_clicked:
            # Perform transcription when the button is clicked
            transcript = process_transcription(audio_file)

            if transcript:
                # Handle keyword search and sentiment analysis
                handle_keyword_search(transcript)
                handle_sentiment_analysis(transcript)
            else:
                st.error("Transcription failed.")
