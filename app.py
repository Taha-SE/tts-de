import os
from fastapi import FastAPI
from TTS.api import TTS
import gradio as gr

# 1) Ausgaben-Ordner
os.makedirs("outputs", exist_ok=True)

# 2) Modell EINMAL beim Start laden (CPU)
tts = TTS(model_name="tts_models/de/thorsten/vits").to("cpu")

def generate_audio(text="Das ist ein Text"):
    out_path = "outputs/output.wav"
    tts.tts_to_file(text=text, file_path=out_path)
    return out_path

# 3) Gradio-UI
demo = gr.Interface(
    fn=generate_audio,
    inputs=[gr.Text(label="Text")],
    outputs=[gr.Audio(label="Audio")]
)
demo.launch()

fastapi_app = FastAPI()
app = gr.mount_gradio_app(fastapi_app, demo, path="/")