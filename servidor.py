import socket
import threading
import time
contador_clientes = 0 # recurso compartido
lock = threading.Lock()
def handle_client(conn, addr):
	global contador_clientes
	name = conn.recv(1024).decode()
	
	with lock:
		# Incremento del contador
		contador_clientes += 1
		numero = contador_clientes
	print(f"Cliente conectado desde{addr}")
	time.sleep(10)
	response = f"Hola {name}, Eres el cliente numero {contador_clientes} en conectarse a un servidor concurrente!"
	conn.sendall(response.encode())
	conn.close()
	
	

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.1.1", 5000))
server.listen()

print("Servidor concurrente esperando...")

while True:
	conn, addr = server.accept()
	
	#Create a thread per client
	client_thread = threading.Thread(
		target = handle_client, 
		args = (conn,addr)
	)
	client_thread.start() 
