import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

engine.say("Text to speech system with speed control")
engine.runAndWait()