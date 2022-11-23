from num2words import num2words
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/{lang}/{number}")
async def root(lang, number):
    return {"message": num2words(number, lang=lang)}

