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





