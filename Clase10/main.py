from fastapi import FastAPI, HTTPException
import database
from redis_client import r
from producer import enviar_evento

app = FastAPI()

@app.post("/crear_cita")
async def crear_cita(horario: str):
    # 1. Validación con Redis (Lock para evitar duplicidad)
    lock = r.set(f"cita:{horario}", "ocupado", nx=True, ex=3600)
    if not lock:
        raise HTTPException(status_code=400, detail="Horario ocupado en Redis")

    # 2. Guardar en SQLite (Persistencia en WSL) 
    try:
        conn = database.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO citas (horario, estado) VALUES (?, ?)", (horario, 'confirmada'))
        conn.commit()
        conn.close()
    except Exception:
        r.delete(f"cita:{horario}") # Liberamos el lock si la DB falla
        raise HTTPException(status_code=400, detail="El horario ya existe en la base de datos")

    enviar_evento(f"Cita CREADA para {horario}") 
    return {"mensaje": f"Cita para {horario} creada y guardada en WSL"}

@app.post("/cancelar_cita")
async def cancelar_cita(horario: str):
    # 1. Eliminar de la Base de Datos SQLite 
    conn = database.conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE horario = ?", (horario,))
    filas = cursor.rowcount
    conn.commit()
    conn.close()

    if filas == 0:
        raise HTTPException(status_code=404, detail="No se encontró la cita para cancelar")

    # 2. Liberar el horario en Redis 
    r.delete(f"cita:{horario}")
    
    enviar_evento(f"Cita CANCELADA para {horario}") 
    return {"mensaje": f"Cita de las {horario} cancelada exitosamente"}