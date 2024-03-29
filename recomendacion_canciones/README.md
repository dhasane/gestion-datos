# Gestion de datos

## integrantes 
- Daniel Hamilton-Smith	
- Juanita Caballero

## alcance y caracteristicas
El sistema realiza recomendacion de canciones con base a una canción seleccionada por el usuario. Alternativamente también se puede generar una recomendación con base el un perfil de usuario, aunque esto no está disponible desde el front.

## organizacion repositorio

recomendacion_canciones:
- base_config.py: configuracion para entrenamiento y carga de modelo
- db_models.py: modelos de base de datos
- front.py: configuracion front
- rec_model.py: modelo usado para la recomendación
- rest.py: configuración para servidor rest
- song_rec.py: entrenamiento del modelo
- wrapper.py: inicializa servidor uvicorn

## prerequisites

1. Run `docker compose up` using this config [docker-compose.yaml]( https://github.com/dhasane/gestion-datos/blob/main/docker-compose.yml ), this creates a container running Postgres.
2. Run this [jupyter notebook]( https://github.com/dhasane/gestion-datos/blob/main/entrega.ipynb ), this cleans the data and stores it into the database. This notebook consumes two files artists.csv and tracks.csv.

## Installation

1. Install [poetry]( https://python-poetry.org/ ).
2. Run `poetry install`.

## Run the server
There are two alternatives to running the server.

### REST API
Run `poetry run rest`

#### Testing the api

##### Predict by song
This receives a get request with the id of the song as a path parameter.
```
GET /predict_by_song/{song_id} HTTP/1.1
```

##### Predict by user
This receives a post request with a json containing the information of the preferences from the user.
```
POST /predict_by_user HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

[
	{
        "popularity": 0,
        "explicit": 0,
        "danceability": 0,
        "energy": 0,
        "key": 0,
        "loudness": 0,
        "mode": 0,
        "speechiness": 0,
        "acousticness": 0,
        "instrumentalness": 0,
        "liveness": 0,
        "valence": 0,
        "tempo": 0,
        "time_signature": 0
	}
]
```

### Front
Run `poetry run front`

This will deploy the front using gradio.
