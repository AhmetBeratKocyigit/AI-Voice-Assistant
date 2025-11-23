# 🤖 AI-Voice-Assistant-Gemini


![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-API-blue?logo=google)
![SpeechRecognition](https://img.shields.io/badge/Speech_Recognition-Enabled-green)
![License](https://img.shields.io/badge/License-Free-lightgrey)

A lightweight & responsive voice assistant triggered by a single key.  
Speak → Understand → Answer.  
Fast. Smart. Hands-free.

</div>

---

## ✨ Features

- 🎧 Real-time speech recognition (Google Speech API)  
- 🗣️ Natural TTS responses via pyttsx3  
- 🤖 Gemini 2.5 Flash integration  
- ⌨️ Activate with **Home** key  
- 🔄 Live loop listening & responding  
- 🚨 Stable error handling for network/API issues  
- ⚡ Low latency, simple codebase, highly modifiable  

---

## 🛠️ Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Dependencies

Install all necessary Python libraries:

```bash
pip install speech-recognition pyttsx3 keyboard python-dotenv google-genai
```

## 2. API Key Configuration

For security, the API key must be stored in an external `.env` file.

Obtain your free Gemini API key from the Google AI Studio.

Create a file named `.env` in the project's root directory.

Add your API key to this file in the following format:

``` bash
# .env
GEMINI_API_KEY="AIzaSy...YourRealAPIKey...d7F_o"
```

------------------------------------------------------------------------

## ▶️ Usage Guide

### 🚀 Starting the Assistant

Run the Python script:

``` bash
python SesliAsistan.py
```

Activate:\
Press the **Home key** once. The assistant will say "Starting assistant"
and begin listening.

------------------------------------------------------------------------

## 🎤 Voice Commands

When listening is active, you can use built‑in commands or ask
questions.

### Special Voice Commands 

| Category | Command (Voice) | Example | Function |
| :---: | :---: | :--- | :--- |
| **Special Commands** | `Time` | *"What time is it?"* | Speaks the current time. |
| | `Lumos` / `Nox` | *"Lumos"* | Triggers custom light/flashlight commands. |
| | `Your Name` | *"What is your name?"* | States the assistant's name (`maNas`). |
| **Stop Assistant** | `Stop` / `Exit` / `Shut down` | *"Stop"* | Terminates the assistant's listening loop. |
| **Gemini Query** | *General Question* | *"Explain quantum computing simply"* | Sends the query to Gemini and speaks the AI response. |

---

## ⏹️ Stopping the Assistant

Two ways to stop:

-   Press **Home** again.\
-   Say **"Stop"** or **"Exit"**.

------------------------------------------------------------------------

## 🧩 Project Structure

| File / Section | Description |
| :--- | :--- |
| **Main Loop** | Uses `keyboard.read_event()` to monitor the **`Home`** key and manages the assistant's active state robustly. |
| `listen()` | Opens the microphone, performs **English** speech recognition (`en-US`), and converts speech to text. |
| `respond()` | Checks for custom commands (`time`, `lumos`, etc.); otherwise, sends the prompt to Gemini with a **100-token output limit**. |
| `client` Initialization | Initializes the Gemini API connection by securely retrieving the `GEMINI_API_KEY` from the **`.env`** file. |
