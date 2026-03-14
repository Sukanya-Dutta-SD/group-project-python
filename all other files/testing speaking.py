import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Speak something (say exit to stop)...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        if text.lower() == "exit":
            break

        engine.say(text)
        engine.runAndWait()

    except:
        print("Sorry, I could not understand.")