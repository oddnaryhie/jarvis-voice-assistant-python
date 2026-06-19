import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "pub_132711508b8546e38dae3e17612e1ba5"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def procesCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif"open Youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open Linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)

    # elif "news" in c.lower():
    #     r = requests.get( "https://newsdata.io/api/1/latest?apikey=pub_132711508b8546e38dae3e17612e1ba5&country=us&category=technology")

    

        

if __name__== "__main__":
    speak("Intializing Jarvis.....")
    #Listten for the wake word Jarvis
    while True:
        r = sr.Recognizer()
        print("recogning...")

      
        # recognize speech using google

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if (word.lower()== "jarvis"):
                speak("ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    procesCommand(command)
        except Exception as e:
            print("error; {0}".format(e))
# 