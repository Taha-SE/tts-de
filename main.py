from TTS.api import TTS
tts_manager = TTS().list_models()
all_models = tts_manager.list_models()
print(all_models)