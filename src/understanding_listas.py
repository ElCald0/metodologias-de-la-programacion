"""las listas nos permiten almacenar informacion en un lugar 
la cantidad que se desen: ya sean pocos elementos o millones  de elementos

Una lista es una colecion de items (elementos) que tiene un orden particular. 
se pueden crear listas que incluyan strings, enteros, floats, los nimmbres de las 
personas de tu familia  podemos almacenar (los tipos de datos permitidos en python )
 lo que queramos en una lista
"""

## son elementos mutables: puede modificarse el tamaño de la lista 

#### REGLAS 
"""
*en ingles, 
*en minusculas, 
*en lower_snake (con '_'), 
*se recomienda nombrar una variable de tipo lista en plural 
*En python los corchetes[] indican una lista
sus  elementos se separan con comas

"""

# ejemplo de lista 

bicycles = ["trek", "cannodale", "redline", "specialized", "wheel"]
print (bicycles)

## como acceder a los elemntos de una lista?
"""
Las lista son colecciones ordenadas 
se pueden acceder a un solo elemnto de una lista 
diciendole a python la posicion del elemnto deseado

Para obtener el valor deseado, se debe escribir el nombre de la lista
seguido del indice del elemnto 

"""

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3], bicycles[4])
"""cuando es 'print(bicycles) es una variable tipo lista'
   cuando especificas que elemto de la lista 'print(bicycles[1]) se vuelve una vairable  tipo string' """

## Tambien se pueden poner Floats y enteros 
"""
bicycles = ["trek", "cannodale", "redline", "specialized", "wheel", 3.23, 67]
print(bicycles[6])
print(bicycles[5])

"""

bicycles = ["trek", "cannodale", "redline", "specialized", "wheel"]
print(bicycles[0].upper())
## empiezan en  0 las listas
#######
# como acceder al ultimo elemnto de la lista
print(bicycles[-1])
print(bicycles[-2])
"""0, 1, 2, 3, 4 para los elemntos en orden 
   -1, -2, -3, -4, para ir desde el ultimmo al primero"""

## Utilizar  vlaores de una lista

message = f"mi primera bicicleta fue una con {bicycles [-1]}"
print(message)

## como esta lista es de variable string se pueden poner sus metodos"metodos strings"
message = f"mi primera bicicleta fue una con {bicycles [-1].upper()}"
print(message)






