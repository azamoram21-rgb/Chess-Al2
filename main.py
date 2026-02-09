import random
from objetos import Jugador, Tablero
from funciones import reglas, traductor_movimiento, parametrizacion_mov, encontrar_pieza_mover



nombre1 = str(input("Ingrese el nombre, jugador1: "))
nombre2 = str(input("Ingrese el nombre, jugador2: "))
preferencia = random.randint(0,1)

if preferencia == 0:
    jugador1 = Jugador(nombre1, "blancas")
    jugador2 = Jugador(nombre2, "negras")
    print(f"{jugador1} jugará blancas")
    print(f"{jugador2} jugará negras")
else:
    jugador1 = Jugador(nombre2, "blancas")
    jugador2 = Jugador(nombre1, "negras")
    print(f"{nombre1} jugará blancas")
    print(f"{nombre2} jugará negras")

print("COMENCEMOOOOOOS")
reglas()
tablero = Tablero()
seacabo = False
tablero.agregar_piezas(jugador1, jugador2)
tablero.printear()




print(f"Turno de {jugador1.nombre}")
movimiento = str(input("movimiento: ")).upper()
jugada = traductor_movimiento(movimiento)
rectificador = encontrar_pieza_mover(jugada, jugador1)
print(rectificador)
if rectificador:
    param_jugada = parametrizacion_mov(jugada)
    tablero.limpiar()
    tablero.agregar_piezas(jugador1, jugador2)
    tablero.printear()
