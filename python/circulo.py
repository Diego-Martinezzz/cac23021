import math
class Circulo():

    pi = math.pi
    def __init__(self, r):
        self.r=r

    def __str__(self):
        return f"Circulo de radio:{self.r}"

    def diametro(self):
        return self.r * 2

    def area(self):
        return Circulo.pi * self.r**2
    
    def cambiarRadio(self,r):
        self.r = r
        return f"Circulo de radio: {self.r}"
    

radio = float(input("Ingrese radio:"))

circulo1= Circulo(radio)
print(circulo1)


mi_numero = 5
mi_numero = int(input(["Ingrese un numero"]))
print(mi_numero)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)