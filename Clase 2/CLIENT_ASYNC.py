import asyncio  # Librería para programación asíncrona
import time     # Librería para medir tiempo

async def main():
    # Abre conexión con el servidor
    reader, writer = await asyncio.open_connection(
        "127.0.0.1", 5000
    )

    # Solicita el nombre al usuario
    name = input("Ingresa tu nombre: ")

    # Guarda el tiempo inicial
    start_time = time.time()

    # Envía el nombre al servidor
    writer.write(name.encode())

    # Asegura que el mensaje se envíe completamente
    await writer.drain()

    # Espera respuesta del servidor
    data = await reader.read(1024)

    # Guarda el tiempo final
    end_time = time.time()

    
    # Muestra respuesta del servidor
    print(f"\n--- Resultado para: {name} ---")
    print(f"Respuesta: {data.decode()}")
    
    # Imprime los tiempos (usamos round para que no salgan tantos decimales)
    print(f"Tiempo inicial: {round(start_time, 4)}")
    print(f"Tiempo final:   {round(end_time, 4)}")
    
    # Calcula y muestra el tiempo total de atención (RTT)
    tiempo_total = end_time - start_time
    print(f"Tiempo total de atención: {round(tiempo_total, 2)} segundos")
    print("-" * 30)

    # Cierra la conexión
    writer.close()
    await writer.wait_closed()

# Ejecuta el cliente
asyncio.run(main())
