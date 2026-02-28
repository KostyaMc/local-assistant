from asr import listen
from vosk import Model, KaldiRecognizer
import pyaudio
from tasks.schelduler import create_task
import time


STOP_WORD = ["стоп", "стоп мне неприятно"]

#states = ["listen", "listen_task"]

model = Model(lang="ru")
# Запускает модель распознавания речи с частотой дискретизации 16000 Гц (16 кГц), общепринятой частотой дискретизации для распознавания речи
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

tasks = []

print("Ассистент слушает...")

while True:
    try:
        result = listen(stream=stream, recognizer=recognizer)
        
        if result != None:
            
            # Проверка на стоп слово
            if result["text"] in STOP_WORD:
                print("Текст:", result["text"])
                break
            
            # создание задачи
            if result["text"] == "создать задачу":
                recognizer.Reset() # сброс текста
                time.sleep(1)
                print("Текст:", result["text"])
                command = listen(stream=stream, recognizer=recognizer)
                print("[DEBUG] Начало прослушивания...")
                task = create_task(tasks=tasks, text=command)
                print(f"[DEBUG] Распознано: {command['text']}")
                print(task)
            
            print("Текст:", result["text"])
    except KeyboardInterrupt:
        print("Кто то попытался физически отключить ассистента ")
            