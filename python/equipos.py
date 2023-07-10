# class Equipo atributos: nombre, jugadores(lista), max_jugadores
#                         metodo  __init__(self, nombre, max_jugadores)
#                                 agregar_jugador(self,jugador)

class Equipo():
    def __init__(self, nombre, max_jugadores):
        self.nombre = nombre
        self.max_jugadores = max_jugadores
        self.jugadores = []

    def agregar_jugadores(self,jugador):
        if len(self.jugadores) < self.max_jugadores:
            self.jugadores.append(jugador)
        else:
            print("Error: se excedió la cantidad máxima de jugadores")

    def __str__(self):
        
        cad = f"Nombre Equipo: {self.nombre} Cantidad Maxima Jugadores : {self.max_jugadores}" 

        for jugador in self.jugadores:
            cad += jugador + ", "
        
        return cad
