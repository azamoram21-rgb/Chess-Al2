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
    

class Peon(pieza):
    def __init__(self, posicion, tipo):
        super().__init__(posicion, tipo)
        self.se_movio = False


    def mover(self, nueva):
        movement = traductor_movimiento(nueva)
        if movement != 0:
            if (movement[0] == "P" or movement[0] == "p"):
                # Caso come
                if movement[3]:
                    pass
                else:
                    cords = parametrizacion_mov([movement[1], movement[2]])
                    param_x = cords[0] - int(self.posicion[0])
                    param_y = cords[1] - int(self.posicion[1])
                    if not self.se_movio and param_y == 0 and abs(param_x) == 2:
                        self.se_movio == True
                        self.posicion = [cords[0], cords[1]]
                        return True
                    elif param_y == 0 and abs(param_x) == 1:
                        self.posicion = [cords[0], cords[1]]
                        return True 
                    else:
                        return False
              

class Arfil(pieza):
    def __init__(self, posicion, tipo):
        super().__init__(posicion, tipo)

    def mover(self, nueva):
        movement = traductor_movimiento(nueva)
        if movement != 0:
            if (movement[0] == "A" or movement[0] == "a"):
                # Caso come
                if movement[3]:
                    pass
                else:
                    cords = parametrizacion_mov([movement[1], movement[2]])
                    param_x = cords[0] - int(self.posicion[0])
                    param_y = cords[1] - int(self.posicion[1])
                    print(param_y)
                    print(param_x)
                    print(cords)
                    if (abs(param_x) - abs(param_y)) == 0 and param_x != 0 and param_y != 0:
                        self.posicion = [cords[0], cords[1]]
                        return True
                    else: 
                        return False
                    
              


class Jugador:

    def __init__(self, nombre:str, color:str):
        self.color = color
        self.nombre = nombre
        self.jaque = False
        self.piezas = []
        self.muertas = []

        if self.color == "blancas":
            # Tomar en cuenta que el tablero es de 8x8
            caballo1 = Caballo(posicion = ["7", "6"], tipo = "CB")
            caballo2 = Caballo(posicion = ["7", "1"], tipo = "CB")
            peon1 = Peon(posicion = ["6", "0"], tipo = "PB")
            peon2 = Peon(posicion = ["6", "1"], tipo = "PB")
            peon3 = Peon(posicion = ["6", "2"], tipo = "PB")
            peon4 = Peon(posicion = ["6", "3"], tipo = "PB")
            peon5 = Peon(posicion = ["6", "4"], tipo = "PB")
            peon6 = Peon(posicion = ["6", "5"], tipo = "PB")
            peon7 = Peon(posicion = ["6", "6"], tipo = "PB")
            peon8 = Peon(posicion = ["6", "7"], tipo = "PB")
            arfil1 = Arfil(posicion = ["7", "2"], tipo = "AB")
            arfil2 = Arfil(posicion = ["7", "5"], tipo = "AB")
            self.piezas.append(caballo1)
            self.piezas.append(caballo2)
            self.piezas.append(peon1)
            self.piezas.append(peon2)
            self.piezas.append(peon3)
            self.piezas.append(peon4)
            self.piezas.append(peon5)
            self.piezas.append(peon6)
            self.piezas.append(peon7)
            self.piezas.append(peon8)
            self.piezas.append(arfil1)
            self.piezas.append(arfil2)

        else:
            caballo1 = Caballo(posicion=["0", "6"], tipo="CN")
            caballo2 = Caballo(["0", "1"], "CN")
            peon1 = Peon(["1", "0"], tipo = "PN")
            peon2 = Peon(["1", "1"], tipo = "PN")
            peon3 = Peon(["1", "2"], tipo = "PN")
            peon4 = Peon(["1", "3"], tipo = "PN")
            peon5 = Peon(["1", "4"], tipo = "PN")
            peon6 = Peon(["1", "5"], tipo = "PN")
            peon7 = Peon(["1", "6"], tipo = "PN")
            peon8 = Peon(["1", "7"], tipo = "PN")
            arfil1 = Arfil(posicion = ["0", "2"], tipo = "AN")
            arfil2 = Arfil(posicion = ["0", "5"], tipo = "AN")
            self.piezas.append(caballo1)
            self.piezas.append(caballo2)
            self.piezas.append(peon1)
            self.piezas.append(peon2)
            self.piezas.append(peon3)
            self.piezas.append(peon4)
            self.piezas.append(peon5)
            self.piezas.append(peon6)
            self.piezas.append(peon7)
            self.piezas.append(peon8)
            self.piezas.append(arfil1)
            self.piezas.append(arfil2)


