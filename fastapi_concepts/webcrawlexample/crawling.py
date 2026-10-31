import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def display():
    url = "newwebsiteexample"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    data = []

    a = soup.find_all("a",class_="topblockNews__sidebarLink")

    for item in a:
        data.append(item.text)

    return {"news":data}