class Contador():
    def __init__(self):
        self.contador = 0

    def __str__(self):
        return f"Contador: {self.contador}"
    
    def inicializar(self):
        self.contador = 0

    def incrementar(self):
        self.contador+=1

    def decrementar(self):
        self.contador-=1


contador = Contador()
contador.incrementar()
contador.incrementar()
contador.incrementar()
contador.incrementar()
print(contador)