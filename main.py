from fastapi import FastAPI
from fastapi.responses import JSONResponse
from words import words_accordind_host, words_accordind_Dvinyatin, words_accordind_dictionary
import random

app = FastAPI()

def form_correct_format(content):
    return JSONResponse(content=content, media_type="application/json; charset=utf-8")

def get_word_response(words_list):
    content = {"word": random.choice(words_list)}
    return form_correct_format(content)

def get_words_list_response(words_list):
    content = {"words": words_list}
    return form_correct_format(content)

@app.get("/get-so-word")
def get_random_word():
    return get_word_response(words_accordind_dictionary)

@app.get("/get-host-so-word")
def get_random_host_word():
    return get_word_response(words_accordind_host)

@app.get("/get-dvinyatin-so-word")
def get_random_dvinyatin_word():
    return get_word_response(words_accordind_Dvinyatin)

@app.get("/get-all-so-word")
def get_all_words():
    return get_words_list_response(words_accordind_dictionary)

@app.get("/get-all-host-so-word")
def get_all_host_words():
    return get_words_list_response(words_accordind_host)

@app.get("/get-all-dvinyatin-so-word")
def get_all_dvinyatin_words():
    return get_words_list_response(words_accordind_Dvinyatin)
