from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/dohvati-rezultate/{opseg}/{povrsina}")
def dohvati_rezultate(opseg: float, povrsina: float):
    try:
        url = 'http://localhost:8000/izracunaj-pravokutnik/'  # Zamijeni s pravim URL-om prvog servisa
        parametri = {'Opseg ': opseg, 'Povrsina': povrsina}

        response = requests.post(url, json=parametri)
        rezultati = response.json()

        return rezultati

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))