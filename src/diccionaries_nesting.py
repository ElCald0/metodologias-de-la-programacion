#-------------------------------------#
#   NESTING
#-------------------------------------#
"listas de diccionarios, en diccionarios y diccionarios en diccionarios"

#-----------------------------------#
#     LISTAS DE DICCIONARIOS    
#-----------------------------------#
convenant_elite={
    "color": "blue",
    "points": 10,
    "shield":True,
}
covenant_jackal={"color":"gray", "points": 6, "shield": True}
convenant_grunts={"color": "orange", "points": 3, "shield":False}

#--------------------------------------------#
#    NESTING DE LISTA DE DICCIONARIOS
#--------------------------------------------#

COVENANTS=[]
COVENANTS.append(convenant_elite)
COVENANTS.append(covenant_jackal)
COVENANTS.append(convenant_grunts)
print("COVENANTS")
print('\n')

print('looping')
#--------------------------------#
#  looping though the list
#--------------------------------#

for COVENANT in COVENANTS:
    print(COVENANT)
#-------------------------------------------------------------------------------#
#     vamos a crear una flotilla de enemigos (covenant)
#_---------------------------------------------------------------------------#
covenant_fleet=[]
for _ in range(2):
    covenant_fleet.append(convenant_elite)
for _ in range(20):
    covenant_fleet.append(convenant_grunts)
print("flotilla")
print(covenant_fleet)
print("\n")




#
#     NESTING EN LISTA EN UN DICCIONARIO
#     MENU
print("nesting en listas de diccionarios \n")
tacos={
    "tortillas":['maiz','harina'],
    'guisos':['bistek','tripa','pastor']    
}

print(f" Tu has ordenado unos tacos de  {tacos['guisos'][0]}")
print(f' en tortillas de {tacos["tortillas"][1]}')
print('\n')










#----------------------------------------------------------------#
# DICIIONARIO EN DICCIONARIOS
#----------------------------------------------------------------#

user={

    "charly":{
    "firstname": "carlos",
    "middelname": "antonio",
    "lastname":"tovar garcia",
    "kocation":"mexico",
    "age":34
    },
"MRred":{
    "firstname": "lizandro",
    "middelname": "jose",
    "lastname":"ayuaskd",
    "kocation":"mexico",
    "age":18
    }

}

#--------------------------------------------------------------------------#
# LOOPING DE DICCIONARIOS EN DICCIONARIOS
#_-------------------------------------------------------------------------#
for user, user_info in user.items():
    fullname= f"{user_info["firstname"]}{user_info["middelname"]} {user_info["lastname"]}"
    location= user_info["kocation"]
    age=user_info["age"]
    print(f"\n\n el nombre completo de {user} es:")
    print(fullname)
    print(f"\n la ubicacion de {user} es:")
    print(location)
    print(f"\n la edad de {user} es:")
    print(age)



