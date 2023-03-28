import inspect
from pydantic import BaseModel

class RecModel(BaseModel):
    popularity: int
    explicit: int
    danceability: float
    energy: float
    key: int
    loudness: int
    mode: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int

    @staticmethod
    def get_feature_list():
        attributes = inspect.getmembers(RecModel, lambda a:not(inspect.isroutine(a)))
        return [a for a in attributes[2][1]]

    def to_list(self):
        attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        # el [2:] es para evitar que salga 'Config' y '_abc_impl', que son de la clase en si
        return [a[1] for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))][2:]


    # rc = RecModel(popularity=0, explicit=0, danceability=0, energy=0, key=0, loudness=0, mode=0, speechiness=0, acousticness=0, instrumentalness=0, liveness=0, valence=0, tempo=0, time_signature=0)
