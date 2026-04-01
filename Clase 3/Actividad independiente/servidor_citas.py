from fastapi import FastAPI, HTTPException
import asyncio

app = FastAPI(title="Sistema de Citas Médicas")

# RECURSOS COMPARTIDOS
citas_db = []  # Simulación de base de datos
contador_id = 0
lock = asyncio.Lock()

@app.get("/citas")
async def listar_citas():
    """Retorna todas las citas registradas"""
    return {"total": len(citas_db), "citas": citas_db}

@app.post("/citas")
async def crear_cita(paciente: str, especialidad: str, fecha: str):
    """Crea una cita con validación y delay de 2 segundos"""
    global contador_id
    
    # Validación básica
    if not paciente or not especialidad:
        raise HTTPException(status_code=400, detail="Paciente y Especialidad son requeridos")

    # Requisito: Simulación de delay de 2 segundos
    await asyncio.sleep(2)

    async with lock:
        contador_id += 1
        nueva_cita = {
            "id": contador_id,
            "paciente": paciente,
            "especialidad": especialidad,
            "fecha": fecha
        }
        citas_db.append(nueva_cita)
        return {"mensaje": "Cita creada con éxito", "cita": nueva_cita}

@app.get("/citas/buscar/{nombre_paciente}")
async def buscar_por_paciente(nombre_paciente: str):
    """Busca citas filtrando por el nombre del paciente"""
    resultados = [c for c in citas_db if nombre_paciente.lower() in c["paciente"].lower()]
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron citas para este paciente")
    return {"resultados": resultados}

@app.delete("/citas/{cita_id}")
async def cancelar_cita(cita_id: int):
    """Elimina una cita por su ID"""
    global citas_db
    async with lock:
        cita_encontrada = next((c for c in citas_db if c["id"] == cita_id), None)
        if not cita_encontrada:
            raise HTTPException(status_code=404, detail="ID de cita no encontrado")
        
        citas_db = [c for c in citas_db if c["id"] != cita_id]
        return {"mensaje": f"Cita {cita_id} cancelada exitosamente"}
