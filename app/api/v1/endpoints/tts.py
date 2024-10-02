from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.services.tts_service import TTSService

router = APIRouter()

# Initialize the TTS Service
tts_service = TTSService(language="en", slow=False)

@router.post("/tts/", response_class=FileResponse)
async def get_tts(text: str, output_format: str = "mp3"):
    """
    Convert the input text to speech and return the audio file.
    :param text: The text to convert into speech
    :param output_format: Desired audio format ('mp3', 'wav')
    :return: The audio file as a response
    """
    audio_file_path = tts_service.text_to_speech(text, output_format)

    if not audio_file_path:
        raise HTTPException(status_code=500, detail="TTS conversion failed")
    
    return FileResponse(audio_file_path, media_type=f"audio/{output_format}", filename=f"tts.{output_format}")
