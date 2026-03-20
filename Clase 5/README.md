

# Problema

Se desea simular un sistema de reserva de asientos donde múltiples usuarios intentan reservar al mismo tiempo.
El problema ocurre cuando varios hilos acceden y modifican la variable `asientos` al mismo tiempo, generando inconsistencias como valores negativos.

## Solución sin control

Sin mecanismos de sincronización, el sistema presenta condiciones de carrera (race condition), donde Varios hilos leen el mismo valor, Se realizan múltiples decrementos incorrectos

## Solución con Lock

Se utiliza "threading.Lock()" para proteger la sección crítica:


if cont <= usuarios:
		lock.acquire() #entrar a seccion critica
		cont +=1
		print(f"Usuario N#: {cont}, Materias: {dic}")
		lock.release() #Salir de seccion critica

# Ventajas

-Exclusión mutua (solo un hilo accede a la vez)
-Resultados consistentes
-No hay sobreventa de asientos

# Solución con Semáforo

Se utiliza "threading.Semaphore(3)":


sem.acquire() # Entra a zona critica
	if cont <= usuarios:
		
		cont +=1
		print(f"Usuario N#: {cont}, Materias: {dic}")
	sem.release() #Se libera el semaforo

# Ventajas:

-Control de acceso concurrente
-Funciona similar a Lock cuando el valor es 1

# Resultados sin control

/Programs/Python/Python314/python.exe //wsl.localhost/Ubuntu/home/hack/Clase5/ActividadIndependienteParte1.py
Usuario N#: 1, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 2, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 3, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 4, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 5, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 6, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 7, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 8, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 9, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 10, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 11, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 12, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 13, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 14, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 15, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 16, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 17, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 18, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 19, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 20, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 21, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 22, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 23, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 24, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 25, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 26, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 27, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 28, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 29, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 30, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 31, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 32, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 33, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 34, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 35, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 36, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 37, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 38, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 39, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 40, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 41, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 42, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 43, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 44, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 45, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 46, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 47, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 48, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 49, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
Usuario N#: 50, Materias: {'C6', 'C2', 'C8', 'C5', 'C7', 'C3', 'C9', 'C10', 'C1', 'C4'}
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\hack\Clase5> 

# Con Lock

/Programs/Python/Python314/python.exe //wsl.localhost/Ubuntu/home/hack/Clase5/ActividadIndependienteParte2.py   
Usuario N#: 1, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 2, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 3, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 4, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 5, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 6, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 7, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 8, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 9, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 10, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 11, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 12, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 13, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 14, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 15, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 16, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 17, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 18, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 19, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 20, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 21, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 22, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 23, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 24, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 25, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 26, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 27, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 28, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 29, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 30, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 31, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 32, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 33, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 34, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 35, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 36, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 37, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 38, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 39, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 40, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 41, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 42, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 43, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 44, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 45, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 46, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 47, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 48, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 49, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}
Usuario N#: 50, Materias: {'C9', 'C3', 'C4', 'C2', 'C1', 'C7', 'C10', 'C6', 'C8', 'C5'}

# Con Semaforo

/Programs/Python/Python314/python.exe //wsl.localhost/Ubuntu/home/hack/Clase5/ActividadIndependienteParte3.py   
Usuario N#: 1, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 2, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 3, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 4, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 5, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 6, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 7, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 8, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 9, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 10, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 11, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 12, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 13, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 14, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 15, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 16, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 17, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 18, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 19, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 20, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 21, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 22, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 23, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 24, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 25, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 26, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 27, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 28, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 29, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 30, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 31, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 32, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 33, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 34, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 35, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 36, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 37, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 38, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 39, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 40, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 41, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 42, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 43, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 44, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 45, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 46, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 47, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 48, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 49, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}
Usuario N#: 50, Materias: {'C5', 'C6', 'C2', 'C1', 'C10', 'C9', 'C4', 'C8', 'C7', 'C3'}