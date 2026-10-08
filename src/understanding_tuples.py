"""
TUPLAS
-las tuplas son inmutables 
-son listas que no cambian de tamaño
-se utilizan parentesis () para definir la tupla
    
    Ejemplo:
    si tenemos un rectangulo (largo y ancho) que siempre va a tener
    el mismo tamaño podemos asegurar que sus dimenciones no van a cambiar 
    si colocamos sus valores en unas duplas 
"""
dimensions = (200, 500) ## 200 de largo x 500 de ancho
print("tupla original", dimensions)

### aceder a un solo elemento de la tutpla
print(dimensions[1])

#######33 DIR() nos dice los metodos y atributos de una variabale

##listas
food = ["apple", "wathermelon", "pinaple" ]
print(dir(food))

## strings
print(dir("agua"))

# integer
print(dir(1))
#________________________________________________________________________________#
# modificar valor de listas
print("\n")
names= ["juan", "peep", "cerezo", "farid"]
print (names)
names[0] = "mercury"
names[1] = "mercury"
names[2] = "mercury"
print(names)

print("\n")
#___________________________________________________________________________________#
## intentar modificar una tupla
"""
esta operacion no se puede hacer
    dimensions[0]=10
daria type error
"""
#### LOOPING throgh a tuple

for dimension in dimensions:
    print(dimension)
print("\n")
"""
no se puede modificar una tupla pero si se puede 
cambiar su asignacion de la variable que almacena la tupla
"""
print("\n")
dimensions = (200, 500) ## 200 de largo x 500 de ancho
print("tupla original", dimensions)
dimensions=(300, 400)
print("tupla cambiada", dimensions)
print("\n")






















