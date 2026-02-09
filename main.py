import random
from objetos import Jugador, Tablero
from funciones import reglas
nombre1 = str(input("Ingrese el nombre, jugador1"))
nombre2 = str(input("Ingrese el nombre, jugador2"))
preferencia = random.ranint(0,1)

if preferencia == 0:
    jugador1 = Jugador(nombre1, "blancas")
    jugador2 = Jugador(nombre2, "negras")
    print(f"{jugador1} jugará blancas")
    print(f"{jugador2} jugará negras")
else:
    jugador1 = Jugador(nombre1, "negras")
    jugador2 = Jugador(nombre2, "blancas")
    print(f"{jugador2} jugará blancas")
    print(f"{jugador1} jugará negras")

print("COMENCEMOOOOOOS")
reglas()
tablero = Tablero()
seacabo = False
while not seacabo:
    pass
    