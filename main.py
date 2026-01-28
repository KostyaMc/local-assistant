from asr import listen

STOP_WORD = "стоп"

from vosk import Model, KaldiRecognizer
import pyaudio
import json


model = Model(lang="ru")
# Запускает модель распознавания речи с частотой дискретизации 16000 Гц (16 кГц), общепринятой частотой дискретизации для распознавания речи
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)


print("Ассистент слушает...")

while True:
    try:
        result = listen(stream=stream, recognizer=recognizer)
        
        if result != None:
                
            # Проверка на стоп слово
            if STOP_WORD in result["text"]:
                print("Текст:", result["text"])
                break
            print("Текст:", result["text"])
    except KeyboardInterrupt:
        print("Кто то попытался физически отключить ассистента ")
            