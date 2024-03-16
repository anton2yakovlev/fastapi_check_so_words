from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from model import get_word_response, get_words_list_response
from words import words_accordind_host, words_accordind_Dvinyatin, words_accordind_dictionary


app = FastAPI()

@app.get("/")
def docs_redirect():
    return RedirectResponse(url='/docs')

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
