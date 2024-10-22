import streamlit as st
from gtts import gTTS
import os

# Create the audio directory if it doesn't exist
audio_dir = 'audio'
os.makedirs(audio_dir, exist_ok=True)

# Streamlit UI setup
st.title('Text to Speech Converter')
st.write("Enter your text below and click 'Convert to Audio' to save the generated audio.")

# Text input from the user
user_text = st.text_area("Enter the text you want to convert to speech:")

# Convert text to speech when the button is clicked
if st.button("Convert to Audio"):
    if user_text:
        # Use gTTS to convert text to speech
        tts = gTTS(text=user_text, lang='en')
        
        # Define the audio file path
        audio_file_path = os.path.join(audio_dir, 'output.mp3')

        # Save the audio file
        tts.save(audio_file_path)

        # Provide a link to download the audio file
        st.success(f'Audio saved successfully')
        st.audio(audio_file_path, format='audio/mp3')
    else:
        st.warning("Please enter some text.")
