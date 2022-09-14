from operator import truediv
from re import T


list = ["carne", "pollo", "pescado", ]
list.append("arroz")
list.append("huevos")
list.pop()
list.sort()
list.reverse()
list.remove("carne")
print(list)
"---------------------------------------------"
numero = int(input ("ingresa tu edad"))
if numero >= 18:
    print ("eres mayor de edad")
elif numero <=0:
        print("tu edad no puede ser 0")
else:
        print ("eres menor de edad")
print ("termino el intento" )

print("comienzo")
for i in [0, 1, 2]:
    print ("hola ",end="")
print()
print ("Final")