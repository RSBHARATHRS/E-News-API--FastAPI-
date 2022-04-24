from ast import excepthandler, keyword
from hashlib import new
import imp
from multiprocessing.dummy import Array
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

import data

app = FastAPI()
origins = [
    "http://localhost:8100",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"message": "Uvicorn Server is runing"}


@app.get("/E-News/news-feeds")
def getNewsFeeds():
    return {"newsFeeds": data.news}


@app.get("/E-News/news-feeds/{news_id}")
def update_item(news_id: int):
    for news in data.news:
        if news["newsId"] == news_id:
            return {"news": news, "message": "Success"}
    return {"message": "result Not Found"}
