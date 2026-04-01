import asyncio
import httpx

URL_BASE = "http://127.0.0.1:8000"

async def probar_sistema():
    async with httpx.AsyncClient() as client:
        # 1. Crear una cita (Esto tardará 2 segundos)
        print("\n[PROBANDO CREATE] Creando cita para Juan Camilo...")
        res_crear = await client.post(
            f"{URL_BASE}/citas", 
            params={"paciente": "Juan Camilo", "especialidad": "Odontología", "fecha": "2026-04-10"}
        )
        print(f"Respuesta: {res_crear.json()}")

        # 2. Listar citas
        print("\n[PROBANDO LIST] Consultando todas las citas...")
        res_list = await client.get(f"{URL_BASE}/citas")
        print(f"Total en DB: {res_list.json()['total']}")

        # 3. Buscar cita
        print("\n[PROBANDO SEARCH] Buscando citas de 'Juan'...")
        res_search = await client.get(f"{URL_BASE}/citas/buscar/Juan")
        print(f"Encontrados: {res_search.json()}")

        # 4. Cancelar cita
        print("\n[PROBANDO DELETE] Cancelando cita ID: 1...")
        res_del = await client.delete(f"{URL_BASE}/citas/1")
        print(f"Respuesta: {res_del.json()}")

if __name__ == "__main__":
    try:
        asyncio.run(probar_sistema())
    except Exception as e:
        print(f"Error: Asegúrate de que el servidor esté corriendo. {e}")
