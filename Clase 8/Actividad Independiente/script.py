import requests
import threading

# URL de tu API local
URL = "http://127.0.0.1:8000/crear_cita"

def realizar_peticion(user_id):
    """
    Simula a un usuario intentando reservar la cita.
    """
    try:
        response = requests.post(URL)
        if response.status_code == 200:
            print(f"Usuario {user_id}:  ¡ÉXITO! Cita reservada.")
        else:
            print(f"Usuario {user_id}:  FALLO - {response.json()['detail']}")
    except Exception as e:
        print(f"Error en conexión: {e}")

def simulacion_concurrente():
    print("--- Iniciando prueba de concurrencia (5 usuarios al mismo tiempo) ---")
    hilos = []
    
    # Creamos 5 hilos para enviar peticiones simultáneamente
    for i in range(5):
        t = threading.Thread(target=realizar_peticion, args=(i+1,))
        hilos.append(t)
        t.start()

    # Esperamos a que todos terminen
    for t in hilos:
        t.join()
    
    print("--- Prueba finalizada ---")

if __name__ == "__main__":
     
    simulacion_concurrente()
