# main.py
from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI()

API_KEY = os.getenv("POKEMON_TCG_API_KEY")

@app.get("/pokemon/{card_id}")
def get_pokemon_card(card_id: str):
    url = f"https://api.pokemontcg.io/v2/cards/{card_id}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Pokemon TCG API")
    return response.json()
