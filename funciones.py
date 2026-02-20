# Acá van a ir las funciones que usaremos en el main
# Primero letra y luego numero


def reglas():
    print("------REGLAS------")
    print("para mover una pieza en tu turno: CH4")
    print("Esto mueve el Caballo a C4")
    print("Recuerda que tienes que seguir las reglas clásicas del ajedrez")
    print("NO MUEVAS UNA PIEZA FUERA DEL TABLERO")

def mensaje_error_index():
    print("Pon las coordenadas bien...")

def mensaje_error_params():
    print("mueve la pieza dentro del tablero...")

def mensaje_pieza_inex():
    print("Esa pieza ni existe...")

def dentro_tablero(posicion:list):
        if posicion[0] in "ABCDEFGHabcdefgh" and posicion[1] in "12345678":
            return True
        else:
            return False

def traductor_movimiento(movimiento:str):
    try:
        # Caso si come 
        if "x" in movimiento or "X" in movimiento:
            movimiento = [movimiento[0], movimiento[1], movimiento[2], True]
        else:
            movimiento = [movimiento[0], movimiento[1], movimiento[2], False]
        if movimiento[0] in "RDATCPrdatcp":
            if dentro_tablero([movimiento[1], movimiento[2]]):
                return movimiento
            else:
                mensaje_error_params()
                return 0
        else:
            mensaje_pieza_inex()
            return 0
    except Exception:
        mensaje_error_index()
        return 0
    
def parametrizacion_mov(movimiento:list):
    letras = "HGFEDCBA"
    letritas = "hgfedcba"
    for i in range(0, len(letras)):
        if movimiento[0] == letras[i] or movimiento[0] == letritas[i]:
            #esto en forma matriz (fila, columna)
            return [int(movimiento[1]) - 1, i]
        

def encontrar_pieza_mover(lista_params:list, jugador):
    booleano = False
    for pieza in jugador.piezas:
        if lista_params[0] == pieza.tipo[0]:
            if pieza.mover(lista_params):
                booleano = True
                break
    return booleano


def Verifica_come(cord):
    pass

def hay_algo_delante(pieza):
    pass