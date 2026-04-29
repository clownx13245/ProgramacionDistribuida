import pika
import asyncio

# --- FUNCIONES ASÍNCRONAS (Simulan tareas pesadas) ---

async def notificar(mensaje):
    """Simula el envío de un correo o mensaje al usuario."""
    await asyncio.sleep(1) # Simulación de tiempo de red 
    print(f" [NOTIFICACIÓN] Enviada: {mensaje}") 

async def registrar_log(mensaje):
    """Simula el guardado de la actividad en un log externo."""
    await asyncio.sleep(1) # Simulación de escritura en disco 
    print(f" [LOG] Registro guardado: {mensaje}") 

async def procesar_evento(mensaje):
    """Ejecuta las tareas de forma concurrente para ahorrar tiempo."""
    # asyncio.gather permite que notificar y registrar_log corran al mismo tiempo 
    await asyncio.gather(
        notificar(mensaje),
        registrar_log(mensaje)
    ) 

# --- LÓGICA DE MENSAJERÍA (RabbitMQ) ---

def callback(ch, method, properties, body):
    """Se activa cada vez que llega un mensaje a la cola 'eventos'."""
    mensaje = body.decode() 
    print(f"\n [!] Evento recibido: {mensaje}") 
    
    # Ejecuta el bucle de eventos asíncronos para procesar la notificación y el log
    asyncio.run(procesar_evento(mensaje))
    
    print(" [x] Tarea finalizada.")

def main():
    # Conexión al servidor de RabbitMQ en WSL 
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()

    # Nos aseguramos de que la cola exista [cite: 90]
    channel.queue_declare(queue='eventos')

    # MEJORA PARA MÚLTIPLES WORKERS:
    # 'prefetch_count=1' le dice a RabbitMQ que no entregue un nuevo mensaje
    # a este worker hasta que haya terminado de procesar el anterior.
    channel.basic_qos(prefetch_count=1)

    # Configuración del consumo
    channel.basic_consume(
        queue='eventos',
        on_message_callback=callback,
        auto_ack=True # Confirma automáticamente que el mensaje fue recibido 
    )

    print(" [*] Worker escuchando eventos en WSL. Para salir presiona CTRL+C") 
    channel.start_consuming() 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nWorker detenido.") 