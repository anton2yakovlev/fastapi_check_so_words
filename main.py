from fastapi import FastAPI
from words import words
import random

app = FastAPI()

@app.get("/get-so-word")
def read_random_word():
    return {"word": random.choice(words)}
