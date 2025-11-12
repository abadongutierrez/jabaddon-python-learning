import whisper
import tempfile
import os
from gtts import gTTS


def speech_to_text(audio_binary):
    """
    Convert speech to text using OpenAI's Whisper model (offline).

    Args:
        audio_binary: Binary audio data

    Returns:
        Transcribed text string
    """
    # Load Whisper model (using base model for balance of speed and accuracy)
    # You can change to 'tiny', 'small', 'medium', or 'large' based on your needs
    model = whisper.load_model("base")

    # Save audio binary to a temporary file since Whisper expects a file path
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
        temp_audio.write(audio_binary)
        temp_audio_path = temp_audio.name

    try:
        # Transcribe the audio using Whisper
        result = model.transcribe(temp_audio_path)
        text = result['text'].strip()
        print('recognised text:', text)
        return text
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)


def text_to_speech(text, voice=""):
    """
    Convert text to speech using gTTS (Google Text-to-Speech) - generates browser-compatible MP3.

    Args:
        text: Text to convert to speech
        voice: Voice identifier (optional, not used with gTTS)

    Returns:
        Audio binary data in MP3 format
    """

    # Save speech to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
        temp_audio_path = temp_audio.name

    try:
        # Generate speech using gTTS (default is English)
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(temp_audio_path)

        # Validate file exists and has content
        if not os.path.exists(temp_audio_path):
            raise Exception(f"Audio file was not created at {temp_audio_path}")

        file_size = os.path.getsize(temp_audio_path)
        if file_size == 0:
            raise Exception("Generated audio file is empty")

        # Read the generated audio file
        with open(temp_audio_path, 'rb') as audio_file:
            audio_binary = audio_file.read()

        print(f'text to speech conversion complete - {file_size} bytes')
        return audio_binary
    except Exception as e:
        print(f'Error in text_to_speech: {e}')
        raise
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
