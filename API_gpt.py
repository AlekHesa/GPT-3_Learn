from fastapi import FastAPI
import uvicorn
from GPT3 import *
from pydantic import BaseModel

app = FastAPI()

class TEXT(BaseModel):
    text : str

@app.get("/",tags=['Index'])
def Index():
    return {"Content":"Hello World"}


@app.post("/GPT3/Summary",tags=['GPT-3'])
async def summary(text:TEXT):
    rangkum = summarize(text.text)

    return rangkum  


@app.post("/GPT3/image",tags=['GPT-3'])
async def image(text:TEXT):
    gambar = image_process(text.text)

    return gambar






