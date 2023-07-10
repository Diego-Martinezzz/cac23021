print("Hello world")
print("La suma entre 16 y 31 es:", str(3+6) , "hermoso resultado")

edad= 15 
nombre= "Jorge"

#print("edad es", type(edad))
#print("el nombre es: ", nombre, "y es alto")

'''
comentario de bloque
'''
# line comment

"""
docstring documentation
"""

#nombre=input("ingrese un nombre")
#print("el nombre es", nombre)
'''
edad= int( input("ingrese su edad:"))
def suma_numeros(numeros): # Bloque 1
    suma = 0                  # Bloque 2
    for n in numeros:         # Bloque 2
        suma += n                # Bloque 3
        print(suma)              # Bloque 3
    return suma              # Bloque 2
print()
'''


cadena= "codo a codo"
print("codo" in cadena)
print("a" in cadena)
print("a" not in cadena)

nota= float(input("ingrese la nota:"))

while nota < 0 or nota > 10:
    TypeError

if nota < 0 or nota > 10:
    print("nota invalida")
elif nota < 4:
    print("no aprobo")
elif nota < 7:
    print("aprobo")
else:
    print("nota excelente")

for i in range(0,5,1):
    print(i)


num1 = float(input("Ingrese el número:"))
num2 = float(input("Ingrese el número:"))
def sumar(a,b):
    return a+b

print(f"La suma entre {num1} y {num2} es {sumar(num1, num2)} ")

def tablaMultiplicar(n):
    for i in range(1,11,1):
        print(f"{n} x {i} = {n*i}")