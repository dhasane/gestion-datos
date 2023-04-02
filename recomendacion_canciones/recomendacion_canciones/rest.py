from fastapi import FastAPI

from .base_config import BaseConfig
from .rec_model import RecModel

app = FastAPI()
base = BaseConfig()

@app.get("/predict_by_song/{song_id}")
def predict_by_song(song_id):
    print('predict for ', song_id)
    return base.get_recommendation_song(song_id)

@app.post("/predict_by_user")
def predict_by_user(rm: RecModel):
    return base.get_recommendation_user(rm)
