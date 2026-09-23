"""combinacion de string/concatenacion de strings

es la suma de dos strings

"""

first_name = "caldo"
last_name = 'egg'
full_name = first_name + last_name

print(full_name)

full_name = first_name + " " + last_name

print(full_name)

full_name = first_name + " " + last_name

print(full_name.title())

## OTRA FORMA 

print("caldo", "huevo" + " " + "crudo")

"""el primer elemto es un string normal pero despues de la coma es una concatenacion todo esto
sin generar variables"""

print("caldo", "huevo" + "" + "crudo", first_name+" "+last_name)

"""tambien podemos poner las variables que queremos unir sin tener quew crear una nueva variable juntadolas"""

print("caldo", "huevo" + "" + "crudo", first_name.title()+" "+last_name.title())

"""tambien podemos utilizar los metodos de strings al unir las variable"""

message =   "¡hola, "+ full_name.title() + "!"
print (message)

"""otra forma de concatenar"""

####### WHITE SPACE 

"""cualquien string que no se imprime es decir, un espacio (" "), tabuladores (/t) 
y finales de linea (/n) 
los whitespaces se utilizan continuamente para organizar las salidas de texto a 
usuario de tal manera que sea amigable de leer o ver para los usuarios"""

print ("python")
print ("\t python")
print ("\t\t python")
print ("lenguajes: \n python \n C \n Javascripts")


#### CONCATENACION DE STRINGS UTILIZANDO F-STRINGS

gritos_de_elotes = "el mas bueno pa gritar elotes"
the_better = f"{gritos_de_elotes} eeeeeeeeeeeeeeeeeeeeeeeeeelotes "

print (the_better)

qoute = "que buen grito de elotes"
the_better = f"{gritos_de_elotes} ay mama {qoute}"
print (the_better)
###3investigar metodo .join() de los strings



 