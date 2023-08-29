import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try:
            query = self.recognizer.recognize_google(audio)
            print("You said:", query)
            self.respond(query)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
    
    def respond(self, query):
        response = "I'm sorry, I don't have a response for that."
        
        if "hello" in query:
            response = "Hello! How can I assist you?"
        elif "what's your name" in query:
            response = "I am your Voice Assistant."
        elif "time" in query:
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
        elif "exit" in query:
            response = "Goodbye!"
            self.engine.say(response)
            self.engine.runAndWait()
            os._exit(0)
        
        print("Response:", response)
        self.speak(response)
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

assistant = VoiceAssistant()

while True:
    assistant.listen()
