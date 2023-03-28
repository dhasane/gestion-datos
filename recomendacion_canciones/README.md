# Model serving tutorial (FastAPI version)

Deployment instructions:

1. Install [poetry]( https://python-poetry.org/docs/#installation ).

2. Run `poetry install`.

3. Run `poetry run start`

4. Testing the service using a tool like Postman:

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

7. It is also possible to test it from the browser going to URL: http://localhost:8000/
