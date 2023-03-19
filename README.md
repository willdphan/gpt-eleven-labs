# Jarvis, AI Personal Asistant

This repository uses `OpenAI`'s Whisper and `Gradio` to generate audio responses from a personal assistant named Genie.

## Installation

To install `Gradio` and `OpenAI`, use the commands below.

    pip3 install openai
    pip3 install gradio

Or just use this command to install everything for you.

    pip3 install -r requirements.txt

## Usage

Startup the Gradio interface with the command below. On the Gradio interface, simply record some audio acknowledging Jarvis. Jarvis (using OpenAI's whisper model) will provide a response.

    python3 genius.py

Javis's response will be in audio format and will be printed on the interface.

## License

This script is open-source and licensed under the MIT License. For more details, check the [LICENSE](LICENSE) file.
