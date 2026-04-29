import sqlite3

def conectar():
    # Se conecta al archivo local en WSL
    return sqlite3.connect('citas.db')

def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()
    # Tabla para manejar múltiples horarios y estados 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            horario TEXT UNIQUE,
            estado TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Asegura que la tabla exista al iniciar el sistema
inicializar_db()