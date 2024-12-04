# Audio Analyzer

Welcome to the **Audio Analyzer** application, where you can transcribe audio files, search for specific keywords, and analyze sentiment. This guide will help you set up and navigate through the application.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI API key

## Installation

Start by cloning the repository and installing the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Launch the application using Streamlit with the following command:

```bash
streamlit run main.py
```

## Using Audio Analyzer

When you start the application, you'll see the page titled **"🎧 Audio Transcription, Keyword Search & Sentiment Analysis"**. Follow these steps to utilize the application's features:

### Setup

1. **API Key Input**:
   - Input your OpenAI API key into the sidebar under "Upload Settings". This key is necessary for transcription and analysis functions.

2. **File Upload**:
   - In the sidebar, use the file uploader to select and upload an audio file (MP3 or WAV format). The maximum file size allowed is 25 MB.

### Application Features

Once your API key and audio file are ready, the application will guide you through the following processes:

1. **Transcription**:
   - Click the 'Process' button to transcribe the uploaded audio file. The transcription will appear under the "Transcription and Analysis" section of the UI.

2. **Keyword Search**:
   - Enter keywords or phrases to search within the transcript. The application will display the search results, highlighting the detected keywords or phrases.

3. **Sentiment Analysis**:
   - The sentiment of the transcript will be analyzed and displayed. Results include the sentiment type (e.g., happy, upset) and a detailed explanation.

### Interactive Elements

- **Transcription and Analysis**: Displays the transcribed text and allows further interactions for keyword search and sentiment analysis.
- **Keyword and Sentiment Results**: Interactive elements display results and explanations, which are easily accessible by expanding various sections of the UI.