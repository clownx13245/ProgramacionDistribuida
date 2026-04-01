import asyncio

async def enviar_peticion(mensaje):
    reader, writer = await asyncio.open_connection("127.0.0.1", 5000)
    
    writer.write(mensaje.encode())
    await writer.drain()
    
    data = await reader.read(1024)
    print(f"\n[SERVIDOR]: {data.decode()}")
    
    writer.close()
    await writer.wait_closed()

async def menu():
    while True:
        print("\n--- SISTEMA BANCARIO ---")
        print("1. Crear cliente (CREATE)")
        print("2. Actualizar nombre (PUT)")
        print("3. Eliminar cliente (DELETE)")
        print("4. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre del nuevo cliente: ")
            await enviar_peticion(f"CREATE:{nombre}")
        elif opcion == "2":
            id_cli = input("ID del cliente a actualizar: ")
            nombre = input("Nuevo nombre: ")
            await enviar_peticion(f"PUT:{id_cli},{nombre}")
        elif opcion == "3":
            id_cli = input("ID del cliente a eliminar: ")
            await enviar_peticion(f"DELETE:{id_cli}")
        elif opcion == "4":
            break

if __name__ == "__main__":
    asyncio.run(menu())
