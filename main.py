from fastapi import FastAPI
from words import words_accordind_host, words_accordind_Dvinyatin, words_accordind_dictionary
import random

app = FastAPI()

def get_response(words_list):
    return {"word": random.choice(words_list)}

@app.get("/get-so-word")
def get_random_word():
    return get_response(words_accordind_dictionary)

@app.get("/get-host-so-word")
def get_random_host_word():
    return get_response(words_accordind_host)

@app.get("/get-dvinyatin-so-word")
def get_random_dvinyatin_word():
    return get_response(words_accordind_Dvinyatin)
