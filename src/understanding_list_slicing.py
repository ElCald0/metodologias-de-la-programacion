players=["charly", "juan", "limon", "iancarlo"]
print("lista original".upper(), players)
print("\n")
########### SLICING 
print("desde 0:2".upper(), players[0:2]) #charly, juan se imprimen
"""el resuktado del slicing se le conoce como un 'slice'
permite trabajar con un grupo en epecifico de una lista
"""
print("desde 1:4".upper(), players[1:4])
print("desde :3".upper(), players[:3])
print("desde 2:".upper(), players[2:])
print("desde 2:0".upper(), players[2:0])
print("desde -3:0".upper(), players[-3:])
print("\n")
#############################################casos especiales
print("\n casos especiales".upper())
print("Desde 1:6 solo teniendo 4 strings", players[1:6])
print("Desde 6:1 lista vacia", players[6:1])
print("Desde :0 lista vacia", players[:0])

############################################## looping throug a slice3
print("\n LOOPING")
students=["farid","charly", "juan", "limon", "iancarlo"]
for student in students [2:4]:
    print(f"el estudiante {student} es niña")
print(students)

#################################################Como podemos copiar una lista
my_food=["pizza","tacos","flautas"]

my_friend_food=my_food ######## MANERA ERRONEA DE COPIAR UNA LISTA

#### TRES maneras de copiar una lista
#numero 1- usando sliciing
my_friend_food_2 = my_food[:]
#numero 2- usando el metodo .copy()
my_friend_food_3 = my_food.copi()
#numero 3- usando el metodo buil-in list()
my_friend_food_4 = list(my_food)



######## TAREA SLICE[ : : ]






