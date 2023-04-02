from .rec_model import RecModel
from .db_models import Tracks, load_sql_table
from .song_rec import SongRec

# todas
# ['id', 'name', 'popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 'mode_type', 'track_type', 'instrumental_type', 'live_type', 'valence_type', 'release_date']

class BaseConfig:

    # features = ['popularity', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']

    def __init__(self):
        self.features = RecModel.get_feature_list()
        print("feature list:", self.features)

        self.TRACKS_DF = load_sql_table(Tracks)
        self.TracksSongRec = SongRec(self.TRACKS_DF, self.features)
        self.ANNSTR = self.TracksSongRec.train_if_doesnt_exist("tracks")

    def get_recommendation_song(self, song_id: str):
        return self.TracksSongRec.get_song_rec(self.ANNSTR, song_id).tolist()

    def get_recommendation_user(self, rm: RecModel):
        return self.TracksSongRec.get_user_rec(self.ANNSTR, rm.to_list()).tolist()
