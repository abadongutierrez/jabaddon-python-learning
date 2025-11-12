import whisper
import pyttsx3
import tempfile
import os
import time


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
    Convert text to speech using pyttsx3 (offline) and convert to MP3 for browser compatibility.

    Args:
        text: Text to convert to speech
        voice: Voice identifier (optional, uses default if not specified)

    Returns:
        Audio binary data in MP3 format
    """
    from pydub import AudioSegment

    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Set voice if specified
    if voice != "" and voice != "default":
        voices = engine.getProperty('voices')
        # Try to find a matching voice
        for v in voices:
            if voice.lower() in v.name.lower() or voice in v.id:
                engine.setProperty('voice', v.id)
                break

    # Save speech to a temporary WAV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_wav:
        temp_wav_path = temp_wav.name

    # Create temp path for MP3
    temp_mp3_path = temp_wav_path.replace('.wav', '.mp3')

    try:
        # Generate speech and save to WAV file
        engine.save_to_file(text, temp_wav_path)
        engine.runAndWait()

        # Add delay to ensure file is fully written
        time.sleep(0.5)

        # Wait for WAV file to exist and have content
        max_retries = 10
        retry_count = 0
        while retry_count < max_retries:
            if os.path.exists(temp_wav_path) and os.path.getsize(temp_wav_path) > 0:
                break
            time.sleep(0.1)
            retry_count += 1

        # Validate WAV file exists and has content
        if not os.path.exists(temp_wav_path):
            raise Exception(f"WAV file was not created at {temp_wav_path}")

        wav_size = os.path.getsize(temp_wav_path)
        if wav_size == 0:
            raise Exception("Generated WAV file is empty")

        print(f'WAV file generated - {wav_size} bytes')

        # Convert WAV to MP3 using pydub
        print(f'Converting WAV to MP3...')
        audio = AudioSegment.from_wav(temp_wav_path)
        audio.export(temp_mp3_path, format="mp3")

        # Validate MP3 file
        if not os.path.exists(temp_mp3_path):
            raise Exception(f"MP3 file was not created at {temp_mp3_path}")

        mp3_size = os.path.getsize(temp_mp3_path)
        if mp3_size == 0:
            raise Exception("Generated MP3 file is empty")

        # Read the generated MP3 file
        with open(temp_mp3_path, 'rb') as audio_file:
            audio_binary = audio_file.read()

        print(f'MP3 conversion complete - {mp3_size} bytes')
        return audio_binary
    except Exception as e:
        print(f'Error in text_to_speech: {e}')
        # Check if ffmpeg is available
        import shutil
        if not shutil.which('ffmpeg'):
            print('ERROR: ffmpeg is not installed. Please install ffmpeg to use offline TTS.')
            print('Install with: brew install ffmpeg (macOS) or apt-get install ffmpeg (Linux)')
        raise
    finally:
        # Clean up temporary files
        if os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)
        if os.path.exists(temp_mp3_path):
            os.remove(temp_mp3_path)
