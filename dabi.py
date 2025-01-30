import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


engine = pyttsx3.init()
import pyttsx3

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Get Available Voices
voices = engine.getProperty('voices')

# Set Voice
# You can choose a different voice by changing the index (e.g., 0 or 1)
engine.setProperty('voice', voices[0].id)  # Use voices[0] for a male voice, voices[1] for a female voice

# Function to Convert Text to Speech
def speak(text):
    engine.say(text)
    engine.runAndWait()



def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None


def execute_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'search' in command:
        query = command.replace('search', '')
        speak(f"Searching for {query}")
        info = wikipedia.summary(query, 1)
        print(info)
        speak(info)
    else:
        speak("I can't do that yet. I'm still learning!")


if __name__ == "__main__":
    speak("Hello, I am Dabi. How can I help you today?")
    while True:
        command = listen_command()
        if command:
            if 'exit' in command or 'quit' in command:
                speak("Goodbye!")
                break
            execute_command(command)
