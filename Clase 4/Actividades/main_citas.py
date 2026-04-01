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
    """Crea una conexión async con la base de datos """
    return await aiomysql.connect(**DB_CONFIG)

#ENDPOINTS DEL SISTEMA

@app.post("/citas")
async def crear_cita(paciente: str, fecha: str):
    """Crea una nueva cita con una simulación de proceso lento """
    await asyncio.sleep(2) 
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "INSERT INTO citas (paciente, fecha, estado) VALUES (%s, %s, %s)"
    await cursor.execute(query, (paciente, fecha, "activa"))
    await conn.commit() 
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita creada correctamente"}

@app.get("/citas")
async def listar_citas():
    """Obtiene todos los registros de la tabla citas """
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "SELECT * FROM citas" 
    await cursor.execute(query)
    citas = await cursor.fetchall() 
    await cursor.close()
    conn.close()
    return citas 

@app.get("/citas/{paciente}")
async def buscar_cita(paciente: str):
    """Busca una cita por el nombre del paciente y maneja errores 404 [cite: 300, 314]"""
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "SELECT * FROM citas WHERE paciente=%s" 
    await cursor.execute(query, (paciente,))
    cita = await cursor.fetchone() 
    await cursor.close()
    conn.close()
    
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada") 
    return cita 

@app.delete("/citas/{id}")
async def cancelar_cita(id: int):
    """Cambia el estado de una cita a 'cancelada' """
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "UPDATE citas SET estado='cancelada' WHERE id=%s" 
    await cursor.execute(query, (id,))
    await conn.commit() 
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita cancelada"} 
# --- ACTIVIDADES DE CLASE (IMPLEMENTACIÓN SUGERIDA) ---

@app.get("/citas/status/activas")
async def listar_citas_activas():
    """Actividad: Listar solo citas con estado 'activa' """
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
    """Actividad: Cambiar estado de 'cancelada' a 'activa' """
    conn = await get_connection()
    cursor = await conn.cursor()
    query = "UPDATE citas SET estado='activa' WHERE id=%s"
    await cursor.execute(query, (id,))
    await conn.commit()
    await cursor.close()
    conn.close()
    return {"mensaje": "Cita reactivada"}
