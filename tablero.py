import random


class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tablero = [['~' for _ in range(tamaño)] for _ in range(tamaño)]
        self.barco_fila, self.barco_columna = self.colocar_barco()
    
    def colocar_barco(self):
        fila = random.randint(0, self.tamaño - 1)
        columna = random.randint(0, self.tamaño - 1)
        return fila, columna
    
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
        print()
    
    def actualizar_tablero(self, fila, columna, resultado):
        if resultado == "barco":
            self.tablero[fila][columna] = 'B'
        elif resultado == "agua":
            self.tablero[fila][columna] = 'X'
    
    def verificar_disparo(self, fila, columna):
        if fila == self.barco_fila and columna == self.barco_columna:
            return "barco"
        else:
            return "agua"