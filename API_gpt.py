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

@app.post("/GPT3/ag-bot",tags=['GPT-3'])
async def agbot(text:TEXT):
    convo = [
    
    ]
    prompt = """
    You are an AI named AG-BOT that can help user to solve problems and also user can ask you a question about a certain words to know its meaning
    and description. The problem that they can ask is related to Astragraphia needs such as digital printing, information technology, and any
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





