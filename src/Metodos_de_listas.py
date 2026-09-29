##METODOS DE LISTAS
"""
metodos:
-  .append (agrega elementos a la lista)
-  .insert nos ayuda a agregar elemntos a una lista en un indice especifico



"""

momos = ["el tilin", "el pepe", "ete sech", "momazos_271",]
print(momos)

##MEtodo .append

momos.append("momazos pezo pluma")

print(momos)

#LISTA VACIA

momos_2 = [] ##lista vacia
print(momos_2)

when = "haces tus momos en python"
momos_2.append(when)## primer elemento 
momos_2.append("but los escribes mal y te error")## segundo elemnto
momos_2.append("ooooh mi lente de contacto")##tercer elemento 

print(momos_2)

when = "ay que comico que comico "

momos_2.append(when)

print(momos_2)

##################### METODO .incert

super_market = ["huevos", "leche", "pan"]
print("\n lista original")
print(super_market)

super_market.insert(0, "carne")
print("\n lista con algo agregado ")
print(super_market)

super_market.insert(-1, "salsa")
print("\n lista con algo agregado otra vez ")
print(super_market)



