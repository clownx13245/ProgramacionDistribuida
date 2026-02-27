import asyncio  # Importa la librería para programación asíncrona
import threading
contador_clientes = 0 #Recurso compartido
lock = threading.Lock()
# Función que maneja cada cliente (coroutine)
async def handle_client(reader, writer):
    global contador_clientes
    
    # Espera datos del cliente (máximo 1024 bytes)
    data = await reader.read(1024)

    # Convierte los bytes recibidos en texto
    name = data.decode()
    
    with lock:
        # Contador de clientes
        contador_clientes += 1
        numero = contador_clientes
    await asyncio.sleep(5)
    # Construye el mensaje de respuesta
    response = f"Hola {name}, Eres el cliente numero: {numero}"

    # Envía la respuesta al cliente (en bytes)
    writer.write(response.encode())
         

    # Espera a que los datos se envíen completamente
    await writer.drain()

    # Cierra la conexión con el cliente
    writer.close()

# Función principal del servidor
async def main():
    # Crea el servidor en la IP 0.0.0.0 y puerto 5000
    # handle_client será ejecutado por cada nueva conexión
    server = await asyncio.start_server(
        handle_client, "0.0.0.0", 5000
    )

    # Mantiene el servidor activo
    async with server:
        # El servidor queda escuchando indefinidamente
        await server.serve_forever()

# Ejcontador_clientes = contador_clientes += 1ecuta el event loop principal
asyncio.run(main())
