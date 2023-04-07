import gradio as gr
import requests
import tempfile
import os

def text_to_speech(text, voice_id, api_key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": "e6544386341418fa400345857ec819cc",
        "Content-Type": "application/json",
        "accept": "audio/mpeg"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }
    response = requests.post(url, headers=headers, json=data)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(response.content)
        filepath = f.name
    return filepath

def delete_temp_file(filepath):
    os.remove(filepath)

inputs = [
    gr.inputs.Textbox(label="Text"),
    gr.inputs.Textbox(label="Voice ID"),
    gr.inputs.Textbox(label="API Key")
]

output = gr.outputs.Audio(type="numpy")

title = "Eleven Labs Text to Speech"
description = "Convert text to speech using the Eleven Labs API"
examples = [
    ["Hello, how are you?", "voice_id_here", "api_key_here"],
    ["Can you play some music?", "voice_id_here", "api_key_here"]
]

gr.Interface(fn=text_to_speech, inputs=inputs, outputs=output, title=title, description=description, examples=examples, live=False, capture_session=True, on_close=delete_temp_file).launch()