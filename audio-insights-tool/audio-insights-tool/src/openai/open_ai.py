import os
import openai


# Class to interact with OpenAI API
class OpenAI:
    def __init__(self):
        # Set the OpenAI API key from the configuration file
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if openai_api_key is None:
            print("No key was found for Open AI services")

        client = openai.OpenAI(api_key=openai_api_key)
        # Initialize ChatCompletion object for model
        self.chat_model = client.chat.completions
        self.audio_model = client.audio.transcriptions

    # Method to create a chat model using OpenAI chat completion API
    def create_chat_model(self, *args, **kwargs):
        return self.chat_model.create(*args, **kwargs)

    # Method to create a chat model using OpenAI chat completion API
    def create_audio_model(self, *args, **kwargs):
        return self.audio_model.create(*args, **kwargs)
