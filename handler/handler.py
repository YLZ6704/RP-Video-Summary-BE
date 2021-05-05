import moviepy.editor as mp
import speech_recognition as sr
from datetime import datetime


def processVideo(filename):

    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
