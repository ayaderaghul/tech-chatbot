from typing import Dict
from pydantic import BaseModel
from fastapi import FastAPI
import os
from transformers import pipeline

app = FastAPI()
print("Loading tokenizer + model")

TSC = pipeline('text-generation', model='ayaderaghul/datascience-style-completion',
)

print("loaded tokenizer + model")

class Request(BaseModel):
    text: str
class Response(BaseModel):
    text: str

@app.post("/generate", response_model=Response)
def generate(request: Request):
    input=request.text
    output = TSC(input)
    l = len(input)
    result = output[0]['generated_text'][l:]
    return Response(text=result)