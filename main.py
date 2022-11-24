from num2words import num2words
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return "Welcome to the API Page of numwords.us"

@app.get("/api/{lang}/{number}")
async def api(lang, number):
    return {"result": num2words(number, lang=lang)}

