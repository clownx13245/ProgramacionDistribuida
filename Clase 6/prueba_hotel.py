import asyncio
import httpx # type: ignore

# 1. Configuración básica
URL_RESERVAR = "http://127.0.0.1:8000/reservar"
URL_ESTADO = "http://127.0.0.1:8000/estado"
TOTAL_CLIENTES = 30

# El SEMÁFORO es como una puerta que solo deja pasar a 5 personas a la vez
# Esto evita que el servidor se sature (Requisito del PDF)
semaforo = asyncio.Semaphore(5)

async def realizar_reserva(id_cliente):
    # El 'async with semaforo' controla el flujo
    async with semaforo:
        try:
            # AsyncClient es la herramienta para hacer la petición por internet
            async with httpx.AsyncClient() as cliente:
                respuesta = await cliente.get(URL_RESERVAR)
                datos = respuesta.json()
                
                # Mostramos en consola qué pasó con este cliente
                if "mensaje" in datos:
                    print(f"Cliente {id_cliente}: {datos['mensaje']} (Quedan: {datos['quedan']})")
                else:
                    print(f"Cliente {id_cliente}: {datos['error']}")
                    
        except Exception as e:
            print(f"Cliente {id_cliente}: Error de conexión")

async def main():
    print("--- INICIANDO SIMULACIÓN DE 30 CLIENTES ---")

    # Creamos una lista de tareas para los 30 clientes
    tareas = []
    for i in range(1, TOTAL_CLIENTES + 1):
        tareas.append(realizar_reserva(i))
    
    # asyncio.gather lanza todas las tareas al mismo tiempo
    await asyncio.gather(*tareas)

    # Al final, consultamos cómo quedó el hotel
    async with httpx.AsyncClient() as cliente:
        respuesta_final = await cliente.get(URL_ESTADO)
        estado = respuesta_final.json()
        print("\n--- RESULTADO FINAL ---")
        print(f"Habitaciones que quedaron en el hotel: {estado['habitaciones_disponibles']}")

# Esto es lo que arranca todo el script
if __name__ == "__main__":
    asyncio.run(main())