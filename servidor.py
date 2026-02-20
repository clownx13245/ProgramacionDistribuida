import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.1.1", 5000))
server.listen(1)

print("Servidor esperando conexion...")

conn, addr = server.accept()
print("Cliente Conectado:", addr)

conn.sendall(b"camilo ruiz")
conn.close()
