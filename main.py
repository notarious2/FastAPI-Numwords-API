from num2words import num2words
from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

@app.get("/")
async def welcome():
    return FileResponse('intro.html')

@app.get("/{lang}/{number}")
async def api(lang, number):
    return {"result": num2words(number, lang=lang)}

