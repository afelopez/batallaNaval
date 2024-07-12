from tablero import Tablero


class JuegoBatallaNaval:
    def __init__(self, tamaño=5):
        self.tamaño = tamaño
        self.intentos = self.tamaño*2
        self.tablero_jugador = Tablero(tamaño)
        self.tablero_computadora = Tablero(tamaño)
    
    def jugar(self):
        print("¡Bienvenido a Batalla Naval!")
        self.tablero_jugador.imprimir_tablero()

        while self.intentos > 0:
            try:
                fila = int(input(f"Introduce la fila (0-{self.tamaño-1}): "))
                columna = int(input(f"Introduce la columna (0-{self.tamaño-1}):"))

                if fila < 0 or fila >= self.tamaño or columna < 0 or columna >= self.tamaño:
                    print("Coordenadas fuera de rango. Intenta nuevamente.")
                    continue

                resultado = self.tablero_computadora.verificar_disparo(fila, columna)
                if resultado == "barco":
                    print("¡Felicidades! ¡Hundiste mi barco!")
                    self.tablero_jugador.actualizar_tablero(fila, columna, "barco")
                    break
                else:
                    self.tablero_jugador.actualizar_tablero(fila, columna, "agua")
                    self.intentos -= 1

                self.tablero_jugador.imprimir_tablero()
                print(f"Te quedan {self.intentos} intentos.")
            except ValueError:
                print("Entrada inválida. Por favor, introduce números válidos.")

        if self.intentos == 0:
            print("¡Perdiste! Te quedaste sin intentos.")
            self.tablero_jugador.actualizar_tablero(self.tablero_computadora.barco_fila, self.tablero_computadora.barco_columna, "barco")
            self.tablero_jugador.imprimir_tablero()
            print(f"El barco estaba en la posición ({self.tablero_computadora.barco_fila}, {self.tablero_computadora.barco_columna}).")
