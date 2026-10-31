from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message":"Check out some news with multipages"}

@app.get('/news')
def display(page:int = 1, limit:int = 5):
    
    url = 'https://news.ycombinator.com/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    data = []

    for item in soup.find_all("span",class_="titleline"):
        data.append(item.text)

    start = (page - 1) * limit
    end = start + limit

    return {
        "page":page,
        "limit":limit,
        "total":len(data),
        "data":data[start:end]
    }

