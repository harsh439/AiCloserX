import os
from gtts import gTTS
from typing import Optional
from pydub import AudioSegment
import tempfile

# For advanced TTS (e.g., Google Cloud TTS, AWS Polly), you'd configure credentials here.
# Example: os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/credentials.json'


class TTSService:
    def __init__(self, language: str = "en", slow: bool = False):
        """
        Initialize the TTS Service
        :param language: The language for TTS (default: "en" for English)
        :param slow: Control speed of speech (default: False for normal speed)
        """
        self.language = language
        self.slow = slow

    def text_to_speech(self, text: str, output_format: str = "mp3") -> Optional[str]:
        """
        Convert text to speech using gTTS and return the path to the saved audio file.
        :param text: The text to convert into speech
        :param output_format: Output audio format ('mp3', 'wav', etc.)
        :return: The file path of the audio output or None if conversion fails
        """
        try:
            # Use Google Text-to-Speech (gTTS)
            tts = gTTS(text=text, lang=self.language, slow=self.slow)

            # Use a temporary file to store the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}") as temp_audio_file:
                temp_audio_path = temp_audio_file.name
                tts.save(temp_audio_path)

            # Optionally, convert to other formats (e.g., WAV) using pydub
            if output_format != "mp3":
                temp_audio_path = self.convert_audio_format(temp_audio_path, output_format)

            return temp_audio_path
        except Exception as e:
            print(f"Error during TTS conversion: {e}")
            return None

    def convert_audio_format(self, file_path: str, output_format: str) -> Optional[str]:
        """
        Convert an audio file from MP3 to another format (e.g., WAV).
        :param file_path: The path to the input MP3 file
        :param output_format: The desired output format (e.g., 'wav')
        :return: The new file path with the converted format or None if conversion fails
        """
        try:
            audio = AudioSegment.from_file(file_path, format="mp3")

            # Save the converted file as a new temp file
            converted_file_path = file_path.replace(".mp3", f".{output_format}")
            audio.export(converted_file_path, format=output_format)

            # Optionally, delete the original MP3 file if no longer needed
            os.remove(file_path)

            return converted_file_path
        except Exception as e:
            print(f"Error during audio conversion: {e}")
            return None


# Example usage
if __name__ == "__main__":
    tts_service = TTSService(language="en", slow=False)
    audio_file_path = tts_service.text_to_speech("Hello, this is an example TTS service.", output_format="mp3")

    if audio_file_path:
        print(f"TTS conversion successful. Audio file saved at {audio_file_path}")
    else:
        print("TTS conversion failed.")

"""
Key Features:
gTTS (Google Text-to-Speech):

Converts text into speech using Google's TTS API. This is a free and simple API to convert text to MP3 format.
Adjusts language and speed (slow parameter) during initialization.
Temporary Files:

Saves the generated audio as a temporary file in the specified format.
Returns the file path to the converted audio.
Audio Conversion:

If the output format is different from MP3 (e.g., WAV), the code uses pydub to convert the audio file to the desired format.
Supports converting audio from MP3 to WAV or any other format using AudioSegment from pydub.
Error Handling:

Captures exceptions during both TTS generation and audio conversion, ensuring graceful handling if something goes wrong.
How to Use:
Conversion to MP3: By default, the service converts the text to speech and returns the path to an MP3 file:

python
Copy code
audio_file_path = tts_service.text_to_speech("Hello World!", output_format="mp3")
Conversion to WAV: You can pass a different format (wav) and the service will convert the resulting MP3 to WAV:

python
Copy code
audio_file_path = tts_service.text_to_speech("Hello World!", output_format="wav")
Languages: You can initialize the service with different languages:

python
Copy code
tts_service = TTSService(language="es")  # For Spanish
Requirements:
Install the required libraries using pip:

bash
Copy code
pip install gtts pydub
Note: To use pydub, you also need to have ffmpeg installed. You can install it via:

On Ubuntu/Debian: sudo apt-get install ffmpeg
On macOS: brew install ffmpeg
On Windows, you can download it from ffmpeg.org.
"""