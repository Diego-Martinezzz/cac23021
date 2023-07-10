class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"Nombre {self.nombre} - Edad {self.edad} - DNI {self.dni}"
    
    Persona=juan(dni)
    nombre=input("ingrese nombre:")
    edad=int(input("ingrese edad:"))
    dni=int(input("ingrese dni:"))

        