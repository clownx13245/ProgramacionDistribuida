from fastapi import FastAPI, HTTPException
import redis

# Inicialización de FastAPI
app = FastAPI(title="Sistema de Citas COTECNOVA - SSDD")

# Conexión a Redis
# 'decode_responses=True' es vital para trabajar con strings y no bytes
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Nombre de la clave que actuará como lock distribuido
LOCK_KEY = "cita_10am"

@app.post("/crear_cita")
def crear_cita():
    """
    Intenta crear una cita usando un lock distribuido en Redis.
    nx=True: Solo crea la clave si NO existe (Atomicidad).
    ex=10: La cita expira en 10 segundos para evitar bloqueos infinitos si el sistema falla.
    """
    lock = r.set(LOCK_KEY, "Ocupado", nx=True, ex=10)

    if not lock:
        # Si el lock ya existe, Redis devuelve None
        raise HTTPException(
            status_code=400, 
            detail="Error de Sincronización: La cita ya está reservada por otro proceso."
        )

    return {"mensaje": "Cita creada con éxito", "status": "200 OK", "expira_en": "10s"}

@app.get("/ver_cita")
def ver_cita():
    """
    Consulta el estado actual del recurso en Redis.
    """
    estado = r.get(LOCK_KEY)
    ttl = r.ttl(LOCK_KEY) # Tiempo restante antes de que expire el lock
    
    if not estado:
        return {"mensaje": "La cita está disponible actualmente.", "estado": "Libre"}
    
    return {
        "mensaje": "La cita se encuentra bloqueada.",
        "estado": estado,
        "tiempo_restante_segundos": ttl
    }

@app.delete("/cancelar_cita")
def cancelar_cita():
    """
    Libera el recurso manualmente eliminando la clave de Redis.
    """
    eliminado = r.delete(LOCK_KEY)
    
    if eliminado:
        return {"mensaje": "Cita cancelada correctamente. El recurso ha sido liberado."}
    
    raise HTTPException(
        status_code=404, 
        detail="No se encontró una cita activa para cancelar."
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
