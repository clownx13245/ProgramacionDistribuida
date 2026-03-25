from fastapi import FastAPI
import asyncio

app = FastAPI(title="Sistema de Reservas Hotel Boutique")

# ESTADO COMPARTIDO
habitaciones_disponibles = 8
lock = asyncio.Lock()

@app.get("/estado")
async def consultar_estado():
    """Consulta cuántas habitaciones quedan disponibles"""
    return {"habitaciones_disponibles": habitaciones_disponibles}

@app.get("/reservar")
async def reservar_habitacion():
    """Permite reservar una habitación protegiendo la sección crítica"""
    global habitaciones_disponibles
    
    # SECCIÓN CRÍTICA: Solo un cliente a la vez puede entrar aquí 
    async with lock:
        # Simulación de proceso lento 
        
        await asyncio.sleep(0.2)
        
        if habitaciones_disponibles > 0:
            habitaciones_disponibles -= 1
            return {
                "mensaje": "¡Reservado con éxito!", 
                "quedan": habitaciones_disponibles
            }
        else:
            return {
                "error": "Sin disponibilidad", 
                "quedan": 0
            }

@app.post("/reiniciar")
async def reiniciar_contador():
    """Reinicia el contador a 8 habitaciones """
    global habitaciones_disponibles
    habitaciones_disponibles = 8
    return {"mensaje": "Contador reiniciado a 8"}