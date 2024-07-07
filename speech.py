import sys
import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic,duration=0.2)
            audio = rec.listen(mic)

            txt = rec.recognize_google(audio)
            print(txt)
            if txt == 'quit':
                sys.exit()
    except sr.UnknownValueError:
        rec = sr.Recognizer()
        continue
    except sr.RequestError:
        rec = sr.Recognizer()
        continue