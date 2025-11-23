import speech_recognition as sr
import pyttsx3
from datetime import datetime
import keyboard  
import time  

from dotenv import load_dotenv 
import os

from google import genai
from google.genai.errors import APIError

load_dotenv() 

try:
    api_key = os.getenv("GEMINI_API_KEY") 
    if not api_key:
        raise ValueError("GEMINI_API_KEY, .env dosyasında bulunamadı veya boş.")
        
    client = genai.Client(api_key=api_key)
    print("Gemini istemcisi başarıyla başlatıldı.")
except ValueError as ve:
    print(f"Hata: {ve}")
    client = None
except Exception as e:
    print(f"Gemini istemcisi başlatılamadı: {e}")
    client = None

engine = pyttsx3.init()
engine.setProperty('rate', 160)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5) 
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  
        try:
            text = recognizer.recognize_google(audio, language="en-US") 
            print("Understood: " + text)
            return text
        except sr.UnknownValueError:
            print("Speech unintelligible.")
            return None
        except sr.RequestError:
            print("Could not access Google service (Check internet connection).")
            return None

def respond(command):
    global assistant_active
    
    if 'help' in command:
        speak("How can I assist you?")
    elif 'stop' in command or 'exit' in command or 'shut down' in command:
        speak("Goodbye!")
        return True 
    
    elif client:
        try:
            print("Querying Gemini...")
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=command,
                config=genai.types.GenerateContentConfig(
                    max_output_tokens=100 
                )
            )
            
            ai_response = response.text
            print(f"Gemini Response (Tokens: {len(response.candidates[0].content.parts[0].text.split())}): {ai_response}")
            speak(ai_response)
        
        except APIError:
            speak("Sorry, there is an issue with your API key or the limit has been reached.")
        except Exception as e:
            print(f"An unknown error occurred: {e}")
            speak("I apologize, I cannot access the external service right now.")
            
    return False

def run_assistant_loop():
    global assistant_active
    while assistant_active:   
        command = listen()
        if command:
            if respond(command.lower()):
                assistant_active = False
                break 


if __name__ == "__main__":
    assistant_active = False
    
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'home':
            
            if assistant_active:
                speak("Assistant shutting down.")
                assistant_active = False
                time.sleep(1)
            else:
                speak("Starting assistant.")
                assistant_active = True
                run_assistant_loop()
