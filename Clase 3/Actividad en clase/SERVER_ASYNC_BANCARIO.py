import asyncio

# RECURSOS COMPARTIDOS
clientes_db = {}  # Diccionario para simular base de datos {id: nombre}
contador_global = 0
contador_id = 0   # Para asignar IDs únicos
lock = asyncio.Lock()

async def handle_client(reader, writer):
    global contador_global, contador_id
    
    data = await reader.read(1024)
    mensaje = data.decode().strip()
    
    # Estructura esperada: "COMANDO:VALOR"
    if ":" in mensaje:
        comando, valor = mensaje.split(":", 1)
    else:
        comando, valor = "CREATE", mensaje

    response = ""

    # 1. CREAR CLIENTE (Con delay y validación)
    if comando == "CREATE":
        if not valor: # Requerimiento 3: Validación básica
            response = "Error: El nombre no puede estar vacío."
        else:
            # Requerimiento 5: Simulación de delay de 3 segundos
            await asyncio.sleep(3)
            
            async with lock:
                contador_id += 1
                contador_global += 1 # Requerimiento 4: Contador global
                clientes_db[contador_id] = valor
                response = f"Cliente creado: {valor} (ID: {contador_id}). Total históricos: {contador_global}"

    # 2. ACTUALIZAR NOMBRE (Requerimiento 2: Endpoint PUT)
    elif comando == "PUT":
        try:
            id_cliente, nuevo_nombre = valor.split(",")
            id_cliente = int(id_cliente)
            if id_cliente in clientes_db:
                async with lock:
                    clientes_db[id_cliente] = nuevo_nombre
                response = f"Actualizado: Cliente {id_cliente} ahora es {nuevo_nombre}"
            else:
                response = "Error: ID no encontrado."
        except:
            response = "Error: Formato PUT incorrecto (ID,Nombre)"

    # 3. ELIMINAR CLIENTE (Requerimiento 1: Endpoint DELETE)
    elif comando == "DELETE":
        try:
            id_cliente = int(valor)
            if id_cliente in clientes_db:
                async with lock:
                    nombre_borrado = clientes_db.pop(id_cliente)
                response = f"Eliminado: Cliente {id_cliente} ({nombre_borrado}) fuera del sistema."
            else:
                response = "Error: ID no encontrado."
        except:
            response = "Error: ID inválido."

    writer.write(response.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 5000)
    print("Servidor Bancario Asíncrono iniciado en el puerto 5000...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
