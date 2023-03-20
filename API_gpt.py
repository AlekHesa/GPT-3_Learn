from fastapi import FastAPI
from fastapi import Request
import uvicorn
from GPT3 import *
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TEXT(BaseModel):
    data : str

class TOKEN(BaseModel):
    key : str

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"Message":"Hello World"}
@app.get("/chatbot",response_class=HTMLResponse)
def chatbot(request: Request):
    return templates.TemplateResponse("chatbot.html",{"request":request})

@app.post("/GPT3",tags=['GPT-3'])
async def key(API_KEY : TOKEN):
    api_key= apikey(API_KEY.key)
    return {"Success" : api_key}

@app.post("/GPT3/Summary",tags=['GPT-3'])
async def SUMMARY(text:TEXT):
    
    rangkum = summarize(text.data)

    return rangkum  

@app.post("/GPT3/Test")
def testing(text:TEXT):
    res = text.text

    return res


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

@app.post("/GPT3/code-gen",tags=['GPT-3'])
async def code_generator(text:TEXT):
    generate_code = code_completion(text.text)
    return generate_code





