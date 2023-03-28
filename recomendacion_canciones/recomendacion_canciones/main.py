from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import pandas as pd

from .models import Artists, Genres, ArtistGenres, Tracks, ArtistsTracks, load_sql_table
from .song_rec import SongRec
from .rec_model import RecModel

from fastapi import FastAPI

app = FastAPI()

templates = Jinja2Templates(directory="recomendacion_canciones/templates")

# cols = [column.key for column in Tracks.__table__.columns]
# print(cols)
# ['id', 'name', 'popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 'mode_type', 'track_type', 'instrumental_type', 'live_type', 'valence_type', 'release_date']


print("feature list:", RecModel.get_feature_list())

# features = ['popularity', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']

features = RecModel.get_feature_list()

TRACKS_DF = load_sql_table(Tracks)
TracksSongRec = SongRec(TRACKS_DF, features)
ANNSTR = TracksSongRec.train_if_doesnt_exist("tracks")

@app.get("/", response_class=HTMLResponse)
def hello_world(request: Request):
   return templates.TemplateResponse("index.html", { "request": request })

@app.get("/predict_by_song/{song_id}")
async def predict(song_id):
    print('predict for ', song_id)
    return TracksSongRec.get_song_rec(ANNSTR, song_id).tolist()

@app.post("/predict_by_user")
def make_predictions(rm: RecModel):
    return TracksSongRec.get_user_rec(ANNSTR, rm.to_list()).tolist()

# @app.post("/predict")
# def make_predictions(X: List[DataModel]):
#     print(X)
#     df = pd.DataFrame([x.dict() for x in X])
#
#     predicion_model = PredictionModel()
#     results = predicion_model.make_predictions(df)
#     return results.tolist()
