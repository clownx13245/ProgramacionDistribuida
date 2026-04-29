import pika

def enviar_evento(mensaje):
    #Conectar a RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')

    )

    channel = connection.channel()

    #Crear cola
    channel.queue_declare(queue='eventos')
    #Enviar mensaje
    channel.basic_publish(
        exchange='',
        routing_key='eventos',
        body=mensaje
    )
    print("Evento enviado:", mensaje)
    connection.close()