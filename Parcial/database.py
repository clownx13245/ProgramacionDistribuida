import mysql.connector

def obtener_conexion():
    # Configuración local
    config = {
        "host": "localhost",
        "user": "admin_user",
        "password": "admin123",
        "database": "perfumeria_db"
    }
    return mysql.connector.connect(**config)