import speech_recognition as sr
from datetime import datetime


def processAudio(filename):
    #Speech Recognition库
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        #Google算法
        #还有其他算法
        text = r.recognize_google(audio_data)
        return text
