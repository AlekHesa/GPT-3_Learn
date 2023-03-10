from fastapi import FastAPI
import uvicorn
from GPT3 import *
from pydantic import BaseModel

app = FastAPI()

class TEXT(BaseModel):
    text : str

class TOKEN(BaseModel):
    key : str


@app.get("/",tags=['Index'])
def Index():
    return {"Content":"Hello World"}

@app.post("/GPT3",tags=['GPT-3'])
async def key(API_KEY : TOKEN):
    api_key=apikey(API_KEY.key)
    return api_key

@app.post("/GPT3/Summary",tags=['GPT-3'])
async def SUMMARY(text:TEXT):
    rangkum = summarize(text.text)

    return rangkum  


@app.post("/GPT3/image",tags=['GPT-3'])
async def IMAGE(text:TEXT):
    gambar = image_process(text.text)

    return gambar

@app.post("/GPT3/ag-bot",tags=['GPT-3'])
async def AGBOT(text:TEXT):
    convo = [
    
    ]
    prompt = """
    You are an AI named AG-BOT that can help user to solve problems and also user can ask you a question about a certain words to know its meaning
    and description. The problem that they can ask is related to technologies needs such as digital printing, information technology, and any
    technology related topic. if user ask anything that is not related to the topic mentioned before, do not answer the question and say 'please do not ask anything other than the topic i mention'
    """

    if prompt:
        convo.append({"role":"system","content":prompt})
        if text:
            convo.append({"role":"user","content":text.text})
            response = chatgpt_proc(convo)
            resp = response.choices[0].message.content
            convo.append(
                {"role":"assistant","content":resp}
            )
    return resp, convo





