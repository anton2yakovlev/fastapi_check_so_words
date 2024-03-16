from fastapi.responses import JSONResponse
import random


def form_correct_format(content):
    return JSONResponse(content=content, media_type="application/json; charset=utf-8")

def get_word_response(words_list):
    content = {"word": random.choice(words_list)}
    return form_correct_format(content)

def get_words_list_response(words_list):
    content = {"words": words_list}
    return form_correct_format(content)