import torch
from TTS.api import TTS
import gradio as gr

device = "cpu"

def generate_audio(text="Das ist ein Text"):
    tts = TTS(model_name='tts_models/de/thorsten/vits').to(device)
    tts.tts_to_file(text=text,file_path="outputs/output.wav")
    return "outputs/output.wav"

demo = gr.Interface(fn=generate_audio,inputs=[gr.Text(label="Text"),],outputs=[gr.Audio(label="Audio")])

demo.launch()