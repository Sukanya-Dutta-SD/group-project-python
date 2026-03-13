import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import difflib

# -----------------------------
# Load Knowledge Base
# -----------------------------
with open("knowledge.json", "r") as f:
    knowledge = json.load(f)

# -----------------------------
# Text-to-Speech
# -----------------------------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -----------------------------
# Vosk Speech Recognition Setup
# -----------------------------
model = vosk.Model("vosk-model-small-en-us-0.15")
audio_queue = queue.Queue()
ignore_audio = False  # flag to ignore mic while bot speaks

def callback(indata, frames, time, status):
    if not ignore_audio:
        audio_queue.put(bytes(indata))

recognizer = vosk.KaldiRecognizer(model, 16000)

print("🎤 Voice AI Chatbot Ready (Say 'bye' to exit)")

# -----------------------------
# Helper: Fuzzy Match
# -----------------------------
def get_best_match(user_input, knowledge_keys, threshold=0.7):
    """
    Returns the best matching key from knowledge_keys if similarity >= threshold.
    """
    best_match = None
    highest_ratio = 0
    for key in knowledge_keys:
        ratio = difflib.SequenceMatcher(None, user_input, key).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = key
    if highest_ratio >= threshold:
        return best_match
    return None

# -----------------------------
# Main Loop
# -----------------------------
with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback):

    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            user_input = result.get("text", "").lower().strip()

            if user_input == "":
                continue

            print("You:", user_input)

            # Exit condition
            if "bye" in user_input:
                ignore_audio = True
                speak("Goodbye!")
                break

            # -----------------------------
            # Fuzzy Keyword Matching
            # -----------------------------
            best_key = get_best_match(user_input, knowledge.keys(), threshold=0.7)
            if best_key:
                ignore_audio = True
                speak(knowledge[best_key])
                ignore_audio = False
            else:
                ignore_audio = True
                speak("Sorry, I don't know that yet.")
                ignore_audio = False