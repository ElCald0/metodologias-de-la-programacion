##lsitas  aprender a usar 
adventure_time=["fin", "jake", "marseline", "BMO", "rollo de canela", "mentita", "rey helado"]
print(adventure_time)
print(adventure_time[1], adventure_time[2], adventure_time[0])

print("\n")
########### CICLO: FOR #########################
for adventure_times in adventure_time:
    print(adventure_times)

## Argumento quitando salto de linea
print("\n Argumento quitando salto de linea:")
for adventure_times in adventure_time:
    print(adventure_times, end=" ")
print("\n")
"""esto se le comoce como looping (a el 'for')"""

################# Imprimir un mensaje para cada mago
print("\n")
print("\n INMPRIMIR UN MENSAJE".title())
for adventure_times in adventure_time:
    print(f"{adventure_times.title()} es mi personaje favorito")
print("\n")

print("\n INMPRIMIR dos MENSAJE".title())
for adventure_times in adventure_time:
    print(f"{adventure_times.title()} es mi personaje favorito")
    print(f"cual es mi personaje favorito? {adventure_times.title()}\n")
print("*eso es todo amigos".title())
print("\n")

######### LOs espacios en blanco de python se llama identacion #######
############## IDENTACION
"""python utiliza la idedntacion para determinar cuando una linea de codogo esta 
coectada a la linea de codigo anterior, 

Utiliza 4 espacio en blanco para obligarnos a escribir codigo ordenado y estructurado
"""
print("\n")
adventure_time=["fin", "jake", "marseline", "BMO", "rollo de canela", "mentita", "rey helado"]

################################# Error de Logica - se queria que el ultimo print (sin identacion) de repitiera  
for adventure in adventure_time:
    print(adventure) ## si no pongo el espacio da error de identacion *****************************
print(f"mi personaje favorito {adventure}")

print("\n")

###################################### Error de identacion inesesaria
"""
message = 'hola'
    print(message)

"""

############ Sintax error no olvidar los dos puntos (:) al final del FOR

""" 
for adventure in adventure_time
    print(adventure)
    """





