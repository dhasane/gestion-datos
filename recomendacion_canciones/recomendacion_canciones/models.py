from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import insert

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime

import datetime

engine = create_engine("postgresql+psycopg2://postgresgd:Password@localhost:5432/postgresgd")
engine.fast_executemany = True

class Base(DeclarativeBase):
    pass

class Artists(Base):
    __tablename__ = "artists"

    id: Mapped[str] = mapped_column(primary_key=True)
    followers: Mapped[int]
    name: Mapped[str]  # = mapped_column(String(100))
    popularity: Mapped[int]


class Genres(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)# = mapped_column(String(30))

class ArtistGenres(Base):
    __tablename__ = "artist_genres"
    artist_id: Mapped[str] = mapped_column(ForeignKey("artists.id"), primary_key=True)

    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"), primary_key=True)

    artist: Mapped["Artist"] = relationship(cascade="all, delete")
    genre: Mapped["Genre"] = relationship(cascade="all, delete")

class Tracks(Base):
    __tablename__ = "tracks"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] # = mapped_column(String(100))
    popularity: Mapped[int]
    duration_ms: Mapped[int]
    explicit: Mapped[int]
    # artists                      object
    # id_artists                   object
    release_date = Column(DateTime, default=datetime.datetime.utcnow)
    danceability: Mapped[float]
    energy: Mapped[float]
    key: Mapped[float]
    loudness: Mapped[float]
    mode: Mapped[int]

    speechiness: Mapped[float]
    acousticness: Mapped[float]
    instrumentalness: Mapped[float]
    liveness: Mapped[float]
    valence: Mapped[float]
    tempo: Mapped[float]
    time_signature: Mapped[int]

    mode_type: Mapped[str]
    track_type: Mapped[str]
    instrumental_type: Mapped[str]
    live_type: Mapped[str]
    valence_type: Mapped[str]

class ArtistsTracks(Base):
    __tablename__ = "artist_tracks"
    artist_id: Mapped[str] = mapped_column(ForeignKey("artists.id"), primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"), primary_key=True)


    artist: Mapped["Artist"] = relationship(cascade="all, delete")
    track: Mapped["Track"] = relationship(cascade="all, delete")


import pandas as pd

def load_sql_table(db: Base):
    with engine.connect() as conn:
        return pd.read_sql_table(db.__tablename__, conn)
