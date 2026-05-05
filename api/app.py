from fastapi import FastAPI
from src.ingest import fetch_open_meteo
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Weather API Running"}

@app.get("/weather")
def weather(lat: float, lon: float):
    return fetch_open_meteo(lat, lon)