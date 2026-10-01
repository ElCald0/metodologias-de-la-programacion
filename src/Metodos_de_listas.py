##METODOS DE LISTAS
"""
metodos:
-  .append(*) (agrega elementos a la lista)
-  .insert(*,*) nos ayuda a agregar elemntos a una lista en un indice especifico
-  .pop(*"opcional") Elimina delemntos de una lista por indice si colocas el numero del indique que quieres eliminar
                    si no indicas cual elimina el ultimo pero aun se puede utilizar despues de ser eliminado
-  .remove (*"obligatorio") elimina elemtos de la lista por valor                    



"""

momos = ["el tilin", "el pepe", "ete sech", "momazos_271",]
print(momos)

###########################################################MEtodo .append()

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

############################################################## METODO .incert()

super_market = ["huevos", "leche", "pan"]
print("\n lista original")
print(super_market)

super_market.insert(0, "carne")
print("\n lista con algo agregado ")
print(super_market)

super_market.insert(-1, "salsa")
print("\n lista con algo agregado otra vez ")
print(super_market)

############################################################### METODO .pop()
print("\n metodo pop nuevas cosas")
cinema = ["sopranos", "br", "wishplas", "toystory",]
print(cinema)
cinema.pop() ##elimina toystory
print(cinema)

eliminada = cinema.pop()## elimina wisplash
print(cinema)
print(f"pelicula borrada es: {eliminada}")

cinema.pop()##elimina br
eliminacion_reciente=cinema.pop()## elimina sopranos
print(f"tu ultima pelicula borrada es: {eliminacion_reciente}")


###### indice especifico
print("\n METODO POP ELIMINANDO UN ELEMNTO ESPECIFICO")
cinema = ["sopranos", "br", "wishplas", "toystory",]
print(cinema)
cinema.pop(1)## ELIMINA   br
print(cinema)

eliminada = cinema.pop(-3) ## elimina sopranos
print(cinema)
print(f"pelicula borrada es: {eliminada}")

################################################### METODO REMOVE
print("\n METODO REMOVE")
people = ["cerezo", "farid", "montes", "chark"]
print(people)
people.remove("farid")
print(people)

########## ordenar listas permanentes en orden alfabetico acendento o decendente metodo opcional".sort()"

print("\n ordenar listas".title())
people = ["cerezo", "farid", "montes", "chark"]
print(people)
people.sort()
print(people)

people.sort(reverse=True)
print(people)

## tarea estudiar el metofo de la lista .reverse()
# metodos build-in: sorted(), len()
print("\selecionar elementos de una lista con dos dos listas".upper())
variables = [["suburban","subaru"]["pepe", "juan"]]
print(variables)
print(variables[0])
print(variables[0][1])




