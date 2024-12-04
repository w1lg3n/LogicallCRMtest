import streamlit as st
from src import get_api_key, handle_audio_file


# Streamlit user interface
def main():
    st.set_page_config(page_title="Audio Analyzer", layout="wide")
    st.title("🎧 Audio Transcription, Keyword Search & Sentiment Analysis")
    st.markdown(
        "Easily upload your audio files, search for specific keywords, and analyze the sentiment in just a few clicks."
    )

    # Sidebar for additional options
    with st.sidebar:
        api_key = get_api_key()
        st.header("Upload Settings")
        MAX_FILE_SIZE_MB = 25
        st.write(f"Maximum file size allowed: {MAX_FILE_SIZE_MB} MB")

        # File uploader
        audio_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

    if api_key:
        if audio_file is not None:
            handle_audio_file(audio_file, MAX_FILE_SIZE_MB)
        else:
            st.info("Please upload an audio file to begin.")
    else:
        st.warning("Please enter your OpenAI API key to proceed.")


# Run the app
if __name__ == "__main__":
    main()
