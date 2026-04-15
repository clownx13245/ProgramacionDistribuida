from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.post("/crear_cita")
def crear_cita():
    lock = r.set("cita_10am","Ocupado",nx =True, ex=10)

    if not lock:
        raise HTTPException(status_code=400, detail="Cita ya reservada")

    return {"cita_10am": "Cita creada"}
