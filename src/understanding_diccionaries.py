#--------------------------------------------#
#DICCIONARIOS
#--------------------------------------------#
{ "llave": "valor", "llave"  : "valor"  }

alien_0={"color":"verrde", "point":5}

#diccionario vacio
alien_1={}
#diccionario mas simple
alien_2={"color": "verde"}
print("\n")

#-------------------------------------------------------------------------#
#acceder a los elementos de un dicionario
#-------------------------------------------------------------------------#
print(f"alien 0 es de color: {alien_0['color']}")
print(f"si desvives al alien 0 se te otorgan: {alien_0['point']}")
print("\n")
#-------------------------------------------------------------------------#
#aggregar elementos a un dicionario
#-------------------------------------------------------------------------#
alien_0["x_position"]=25
alien_0["y_position"]=0
print(alien_0)
print("\n")

#-------------------------------------------------------------------------#
#modificar el valor en un diccionario
#-----------------------------------------------------------------------_--#
alien_0["y_position"]=25
print(alien_0)
print("\n")
#--------------------------------------------------------------------------#
#eliminar elementos de un diccionario
#--------------------------------------------------------------------------#
del alien_0["point"]
print(alien_0)
print("\n")

#-------------------------------------------------------------------------#
#diccionario para objetos similares
#------------------------------------------------------------------------#
fav_games= {"cerexo:balatro",
    "farid:zomboid", 
        "caldo:terraria",
    "elliuth:geinshinimpact"}

#-----------------------------------------------------------------------#
#LOOPING though all keyvlues pairs
#looping a traves de todos los pares llave-valor
#-----------------------------------------------------------------------#

user_0={
    "username": "charly",
    "firstname": "tovar",
    "lastname": "garcia",
    "age": 34,
    "birthname":"6-feb"
}
print("looping atravez de los pares llave, valor \n".title())
for key, value in user_0.items():
    print("key", key)
    print("value", value)
print("\n")

print("looping atravez de las llaves \n".title())
for key in user_0.keys():
    print("key", key)
print("\n")

print("looping atravez de los valores \n".title())
for value in user_0.values():
    print("value", value)
print("\n")






