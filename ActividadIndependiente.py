import asyncio
from fastapi import FastAPI, HTTPException
import aiomysql

app = FastAPI(title="Sistema de Citas Médicas - COTECNOVA")

#CONFIGURACIÓN DE CONEXIÓN 
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "", 
    "db": "citas_db"
}

async def get_connection():
    """Crea una conexión async con la base de datos [cite: 238, 239]"""
    return await aiomysql.connect(**DB_CONFIG)

#ENDPOINTS DEL SISTEMA

@app.post("/citas")
async def crear_cita(paciente: str, fecha: str):
    """Crea una nueva cita con una simulación de proceso lento [cite: 263, 265]"""
    await asyncio.sleep(2) 
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "INSERT INTO citas (paciente, fecha, estado) VALUES (%s, %s, %s)"
    await cursor.execute(query, (paciente, fecha, "activa")) [cite: 271]
    await conn.commit() [cite: 272]
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita creada correctamente"} [cite: 275]

@app.get("/citas")
async def listar_citas():
    """Obtiene todos los registros de la tabla citas [cite: 284, 285]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "SELECT * FROM citas" [cite: 288]
    await cursor.execute(query)
    citas = await cursor.fetchall() [cite: 291]
    await cursor.close()
    conn.close()
    return citas [cite: 294]

@app.get("/citas/{paciente}")
async def buscar_cita(paciente: str):
    """Busca una cita por el nombre del paciente y maneja errores 404 [cite: 300, 314]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "SELECT * FROM citas WHERE paciente=%s" [cite: 307]
    await cursor.execute(query, (paciente,))
    cita = await cursor.fetchone() [cite: 309]
    await cursor.close()
    conn.close()
    
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada") [cite: 312, 316]
    return cita [cite: 319]

@app.delete("/citas/{id}")
async def cancelar_cita(id: int):
    """Cambia el estado de una cita a 'cancelada' [cite: 325, 330]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "UPDATE citas SET estado='cancelada' WHERE id=%s" [cite: 330]
    await cursor.execute(query, (id,))
    await conn.commit() [cite: 332]
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita cancelada"} [cite: 335]

# --- ACTIVIDADES DE CLASE (IMPLEMENTACIÓN SUGERIDA) ---

@app.get("/citas/status/activas")
async def listar_citas_activas():
    """Actividad: Listar solo citas con estado 'activa' [cite: 379]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "SELECT * FROM citas WHERE estado='activa'"
    await cursor.execute(query)
    citas = await cursor.fetchall()
    await cursor.close()
    conn.close()
    return citas

@app.put("/citas/reactivar/{id}")
async def reactivar_cita(id: int):
    """Actividad: Cambiar estado de 'cancelada' a 'activa' [cite: 382]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "UPDATE citas SET estado='activa' WHERE id=%s"
    await cursor.execute(query, (id,))
    await conn.commit()
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita reactivada"}
