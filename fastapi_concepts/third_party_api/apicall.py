import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message":"Welcome to Third Party Integration API."}

@app.get('/display')
def display():
    url = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(url)

    return response.json()

@app.get('/display/{pokemon_name}')
def search(pokemon_name:str):
    url = url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    response = requests.get(url)

    return response.json()