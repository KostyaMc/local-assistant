import json


def listen(stream, recognizer):
    """
    Функция преобразует сказанный текст в json формат.
    Возвращает объект json, если была распознана речь.
    Используется только с vosk и pyaudio
    
    :param stream: поток данных микрофона
    :param recognizer: модель распознавания речи
    """
    
    stream.start_stream()
    
    data = stream.read(4096, exception_on_overflow=False) # exception_on_overflow=False предотвращает генерацию исключения в случае переполнения
    if recognizer.AcceptWaveform(data):  # Отправляет аудиоданные в распознаватель речи
        result = json.loads(recognizer.Result())
        return result
