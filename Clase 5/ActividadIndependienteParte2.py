import threading
lock = threading.Lock()
usuarios = 50
dic = {"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"}
cont = 0
def reservar():
	global cont

	if cont <= usuarios:
		lock.acquire() #entrar a seccion critica
		cont +=1
		print(f"Usuario N#: {cont}, Materias: {dic}")
		lock.release() #Salir de seccion critica


for i in range(usuarios):
	threading.Thread(target=reservar).start()
	
