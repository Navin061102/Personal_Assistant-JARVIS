import pyttsx3 ##for the ai to speak,## text to speech library
import datetime
import speech_recognition as sr ##for getting input voices   ## speech to text library
import wikipedia ##for surfing wikipedia
import os  ##for opening local files
import webbrowser ## for surfing the internet

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("It is a fine morning sir !")

    elif hour>=12 and hour<18:
        speak("Hope you had your brunch, Good Afternoon Sir !")

    else:
        speak("The wind is lovely, Good Evening sir !")

    speak("Hello How are you? I am your personel AI Assistant Jarvis! How can I be of service")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  ##speech to text
        print(f"You said: {query}\n")

    except Exception as e:

        print("I could not get you, please speak again")
        return "None"
    return query


if __name__ == "__main__":
    greet()
    # while True:
    if 1:
        query = command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ' instagram' in query:
            webbrowser.open("instagram.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'kaggle' in query:
            webbrowser.open("kaggle.com")


        elif 'the weather' in query:
            webbrowser.open("weather.com")

        elif 'the score' in query:
            webbrowser.open("cricbuzz.com")


        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/?")
            


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open anaconda' in query:
            condapath = "C:\\Users\\khank\\anaconda3"
            os.startfile(condapath)

        elif 'discord' in query:
            calpath = "C:\\Users\\khank\\AppData\\Local\\Discord\\app-1.0.9003"
            os.startfile(calpath)
