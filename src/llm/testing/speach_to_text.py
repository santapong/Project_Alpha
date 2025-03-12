import sounddevice as sd
import queue
import vosk
import json
import os

from langchain.chat_models import init_chat_model

model = vosk.Model(".vosk/model")
q = queue.Queue()

llm = init_chat_model(
    model=os.getenv("LLM_MODEL"),
    model_provider=os.getenv("LLM_PROVIDER"),
    base_url=os.getenv("LLM_BASE_URL"),
)


def callback(indata, frames, time, status):
    if status:
        print(status)
        print("callback")
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, 16000)
    print("Listening...")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            
            print(json.loads(rec.Result()))
            user_text = json.load(rec.Result())
            
            print(llm.invoke(user_text))