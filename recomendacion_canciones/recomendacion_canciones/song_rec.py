from annoy import AnnoyIndex
import pandas as pd
from os.path import exists

class SongRec:
    def __init__(self, df: pd.DataFrame, features):
        self.df = df
        self.features = features

    def train_model(self, name: str, iterations=1000):
        len_features = len(self.features)
        annoy = AnnoyIndex(len_features, "euclidean")

        for i in self.df.index:
            v = self.df.loc[i][self.features].values
            annoy.add_item(i, v)

        annoy.build(iterations, n_jobs=5)

        annstr = "{}.ann".format(name)
        annoy.save(annstr)
        return annstr

    def train_if_doesnt_exist(self, name: str, iterations=1000):
        annstr = "{}.ann".format(name)
        if not exists(annstr):
            print('training and storing in', annstr)
            self.train_model(name, iterations)
            print('training end')
        return annstr

    def get_song_rec(self, annoy_path: str, song_id: str):
        annoy_loaded = AnnoyIndex(len(self.features), "euclidean")
        annoy_loaded.load(annoy_path)
        song = self.df[self.df['id'] == song_id].index
        neighbors = annoy_loaded.get_nns_by_item(song, 10)
        return self.df.loc[neighbors]

    def get_user_rec(self, annoy_path: str, user_vector):
        annoy_loaded = AnnoyIndex(len(self.features), "euclidean")
        annoy_loaded.load(annoy_path)
        neighbors = annoy_loaded.get_nns_by_vector(user_vector, 10)
        return self.df.loc[neighbors]
