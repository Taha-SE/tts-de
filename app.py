import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from TTS.api import TTS
import gradio as gr

# Ausgaben-Ordner
os.makedirs("outputs", exist_ok=True)

# Lazy load: Modell erst laden, wenn wirklich gebraucht
_tts = None
def get_tts():
    global _tts
    if _tts is None:
        _tts = TTS(model_name="tts_models/de/thorsten/vits").to("cpu")
    return _tts

def generate_audio(text="Das ist ein Text"):
    out_path = "outputs/output.wav"
    get_tts().tts_to_file(text=text, file_path=out_path)
    # Gradio erwartet hier den Pfad, damit es die Datei streamen kann
    return out_path

# Gradio-UI (ohne launch!)
demo = gr.Interface(
    fn=generate_audio,
    inputs=[gr.Text(label="Text")],
    outputs=[gr.Audio(label="Audio", type="filepath")]
)

# FastAPI + Gradio mounten
fastapi_app = FastAPI()

@fastapi_app.get("/")
def root():
    return RedirectResponse(url="/gradio")

app = gr.mount_gradio_app(fastapi_app, demo, path="/gradio")
