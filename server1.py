from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/izracunaj-pravokutnik/")
def izracunaj_pravokutnik(duzina: float, sirina: float):
    try:
        povrsina = duzina * sirina
        opseg = 2 * (duzina + sirina)

        rezultati = {
            'povrsina': povrsina,
            'opseg': opseg
        }

        return rezultati

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))