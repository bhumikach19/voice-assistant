import pyttsx3
import speech_recognition as sr

def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    # returning audio as text
    return Query
    
# creating Speak() function to giving Speaking power to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "insta" in command:
            Speak("Best python page on instagram is pythonhub")
        if "learn" in command:
            Speak("udemy is best to learn python")
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break