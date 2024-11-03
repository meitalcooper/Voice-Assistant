# Voice-Assistant

This Python project implements a simple voice assistant capable of understanding and responding to spoken commands. The assistant can provide information, play media, deliver news updates, and report weather conditions based on user interactions.

## Features
- **Information Retrieval:** Fetches and reads information from Wikipedia based on user queries.
- **Media Playback:** Plays videos and music directly from YouTube according to user requests.
- **News Updates:** Provides the latest news from various categories such as business, technology, and global events.
- **Weather Forecasts:** Offers current weather conditions and forecasts for specified locations.

## Technologies Used
- `Python 3`: Main programming language used.
- `pyttsx3`: Python text-to-speech conversion library.
- `speech_recognition`: Library for performing speech recognition, with support for multiple engines and APIs.
- `selenium`: Tool for automating web browsers.
- `requests`: Library for making HTTP requests in Python.

## Setup
To run this project, you will need to install the required Python libraries. Follow these steps:

\```bash
# Clone the repository
git clone https://github.com/meitalcooper/python-voice-assistant.git
cd python-voice-assistant

# Install dependencies
pip install pyttsx3 speech_recognition selenium requests

# Run the application
python main.py
\```

## How to Use
1. Start the application using the command `python main.py`.
2. The voice assistant will greet you and prompt for a command.
3. Speak to the assistant with commands like "what's the weather in New York," "play Beatles on YouTube," or "what's the news today."
