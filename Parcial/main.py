from fastapi import FastAPI, HTTPException
import asyncio
from database import obtener_conexion

app = FastAPI(title="E-commerce Perfumería")

# 1. LISTAR INVENTARIO
@app.get("/inventario")
def listar_inventario():
    conexion = obtener_conexion()
    # dictionary=True es vital para que FastAPI devuelva JSON
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventario")
    resultado = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultado

# 2. CREAR PERFUME 
@app.post("/perfumes")
async def crear_perfume(nombre: str, marca: str, precio: float, stock: int):
    # Simulación de delay de 2 segundos 
    await asyncio.sleep(2)
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO inventario (nombre, marca, precio, stock) VALUES (%s, %s, %s, %s)"
    valores = (nombre, marca, precio, stock)
    
    cursor.execute(query, valores)
    conexion.commit() # commit para guardar los datos
    cursor.close()
    conexion.close()
    
    return {"mensaje": "Perfume registrado exitosamente"}

# 3. ACTUALIZAR STOCK 
@app.put("/perfumes/{id}")
def actualizar_perfume(id: int, precio: float, stock: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "UPDATE inventario SET precio=%s, stock=%s WHERE id=%s"
    valores = (precio, stock, id)
    
    cursor.execute(query, valores)
    conexion.commit()
    
    # Verificación de fila afectada 
    filas_afectadas = cursor.rowcount
    cursor.close()
    conexion.close()
    
    if filas_afectadas == 0:
        raise HTTPException(status_code=404, detail="Perfume no encontrado")
        
    return {"mensaje": "Inventario actualizado localmente"}