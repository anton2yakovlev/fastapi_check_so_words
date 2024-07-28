from fastapi.responses import HTMLResponse, JSONResponse
import random


def form_html_format(content):
    return HTMLResponse(content=content, status_code=200)


def form_json_format(content):
    return JSONResponse(content=content, media_type="application/json; charset=utf-8")


def get_word_response(words_list):
    content = {"word": random.choice(words_list)}
    return form_json_format(content)


def get_words_list_response(words_list):
    content = {"words": words_list}
    return form_json_format(content)
