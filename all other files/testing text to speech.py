import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 10.0)
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:
    text = input("Enter text (type exit to quit): ")

    if text.lower() == "exit":
        break

    speak(text)