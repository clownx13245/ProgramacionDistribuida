import threading
usuarios = 50
dic = {"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"}
cont = 0
def reservar():
	global cont
	if cont <= usuarios:
		cont +=1
		print(f"Usuario N#: {cont}, Materias: {dic}")

for i in range(usuarios):
	threading.Thread(target=reservar).start()
	
