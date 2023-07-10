class Bicicleta():
    def __init__(self, nroSerie, año, precio):
        self.nroSerie = nroSerie
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"Numero de serie: {self.nroSerie}, Año: {self.año} y precio: {self.precio}"
    
class Bicicleteria():
    def __init__(self):
        self.ganancias = 0
        self.cantidad_ventas = 0
        self.bicicletas = []

    def __str__(self):
        return f"Bicicletería y Ganancias: {self.ganancias}, Cantidad de ventas: {self.cantidad_ventas}"
    def stock_bicicletas(self):
        return self.bicicletas
    
    def vender_bici(self, bicicleta):
        self.bicicletas.remove(bicicleta)
        self.cantidad_ventas += 1
        self.ganancias = bicicleta.precio

    def agregar_bicicletas(self, bicicleta):
        self.bicicletas.append(bicicleta)

