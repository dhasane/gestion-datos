import uvicorn

def start():
    """ Wrapper para uvicorn.
    Launched with `poetry run start` at root level"""
    uvicorn.run("recomendacion_canciones.rest:app", host="0.0.0.0", port=8000, reload=True)
