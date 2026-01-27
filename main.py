import pyaudio
import json
from vosk import Model, KaldiRecognizer

STOP_WORD = "стоп"

model = Model(lang="ru")
# Запускает модель распознавания речи с частотой дискретизации 16000 Гц (16 кГц), общепринятой частотой дискретизации для распознавания речи
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Ассистент слушает...")

while True:
    data = stream.read(4096, exception_on_overflow=False) # exception_on_overflow=False предотвращает генерацию исключения в случае переполнения
    if recognizer.AcceptWaveform(data):  # Отправляет аудиоданные в распознаватель речи
        result = json.loads(recognizer.Result())
        # Проверка на стоп слово
        if result["text"] == STOP_WORD:
            print("Текст:", result["text"])
            break
        print("Текст:", result["text"])
