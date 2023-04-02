from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .init import Base

from .rec_model import RecModel

from fastapi import FastAPI

app = FastAPI()

templates = Jinja2Templates(directory="recomendacion_canciones/templates")

base = Base()

@app.get("/", response_class=HTMLResponse)
def hello_world(request: Request):
   return templates.TemplateResponse("index.html", { "request": request })

@app.get("/predict_by_song/{song_id}")
def predict_by_song(song_id):
    print('predict for ', song_id)
    return base.get_recommendation_song(song_id)

@app.post("/predict_by_user")
def predict_by_user(rm: RecModel):
    return base.get_recommendation_user(rm)
