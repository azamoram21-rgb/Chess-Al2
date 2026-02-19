from abc import ABC, abstractmethod
from funciones import traductor_movimiento, parametrizacion_mov
from math import sqrt


class Tablero:
    def __init__(self):
        self.casillas = [["--" for _ in range(9)] for _ in range(9)]
        self.movimiento = 0

    def tabulaziones(self):
        for i in range(0, len(self.casillas)):
            numeros = "12345678X"
            letras = "XHGFEDCBA"
            for j in range(0, len(self.casillas[i])):
                if i != len(self.casillas) - 1 and j == 0:
                    self.casillas[i][j] = numeros[i] + " " 
                elif i == len(self.casillas[i]) - 1 and j != 0:
                    self.casillas[i][j] = letras[j] + " " 

    def agregar_piezas(self, j1, j2):
        for pieza in j1.piezas:
            cord_x = int(pieza.posicion[0])
            cord_y = int(pieza.posicion[1])
            self.casillas[cord_x][cord_y + 1] = pieza.tipo
        for pieza in j2.piezas:
            cord_x = int(pieza.posicion[0])
            cord_y = int(pieza.posicion[1])
            self.casillas[cord_x][cord_y + 1] = pieza.tipo

    def printear(self):
        self.tabulaziones()
        separador_horizontal =  "-" * 46
        print("\n   TABLERO DE JUEGO")
        print(separador_horizontal)
        for fila in self.casillas:
            linea_visible = " | ".join(f"{celda}" for celda in fila)
            print(f"| {linea_visible} |")
            print(separador_horizontal)

    def limpiar(self):
        self.casillas = [["--" for _ in range(9)] for _ in range(9)]
        self.tabulaziones()


class pieza(ABC):
    def __init__(self, posicion:list, tipo:str):
        self.posicion = posicion
        self.tipo = tipo
        self.inmunidad = 0

    @abstractmethod
    def mover(self):
        pass

    
class Caballo(pieza):
    def __init__(self, posicion, tipo):
        super().__init__(posicion, tipo)

    def mover(self, nueva):
        movement = traductor_movimiento(nueva)
        if movement != 0:
            if (movement[0] == "C" or movement[0] == "c"):
                # Caso come
                if movement[3]:
                    pass
                else:
                    cords = parametrizacion_mov([movement[1], movement[2]])
                    # 5,0
                    param_x = cords[0] - int(self.posicion[0])
                    param_y = cords[1] - int(self.posicion[1])
                    value = sqrt(((param_x)**2) + ((param_y)**2))
                    if value != sqrt(5):
                        # print("Así no se mueve el caballito")
                        return False
                    else:
                        self.posicion = [cords[0], cords[1]]
                        return True
    

class peon(pieza):
    def __init__(self, posicion, tipo):
        super().__init__(posicion, tipo)
        self.primer_mov = True


    def mover(self, nueva):
        movement = traductor_movimiento(nueva)
        if movement != 0:
            if (movement[0] == "C" or movement[0] == "c"):
                # Caso come
                if movement[3]:
                    pass
                else:
                    # hacer como se mueve el peor
                    pass
class Jugador:

    def __init__(self, nombre:str, color:str):
        self.color = color
        self.nombre = nombre
        self.jaque = False
        self.piezas = []
        self.muertas = []

        if self.color == "blancas":
            caballo1 = Caballo(posicion=["7", "6"], tipo="CB")
            caballo2 = Caballo(["7", "1"], "CB")
            self.piezas.append(caballo1)
            self.piezas.append(caballo2)
        else:
            caballo1 = Caballo(posicion=["0", "6"], tipo="CN")
            caballo2 = Caballo(["0", "1"], "CN")
            self.piezas.append(caballo1)
            self.piezas.append(caballo2)