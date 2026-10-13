#-------------------------------------------------------------#
#                        if statement
#-------------------------------------------------------------#
cars = ("audi", "bmw", "subaru", "toyota")
for car in cars:
    if car=="audi":
        print(car.upper())
    else:
        print(car)
print("\n")
"""
if condition:
    do something '} acciones verdaderas'
else:
    do something '} acciones falsas'

LA CONDICION ES EL CORAZON DEL 'IF'  
    
"""
#--------------------------------------------#
# El condiconal / CONDITION el corazon del if
#--------------------------------------------#
 ##conditional veradero 
 ##conditionl true
truck="wolf"
print(truck=='wolf')
""" esto es una condicional verdadera"""
 ##conditional falso
 ##conditional false
print(truck == 'ford')
print(truck == 'WolF')
"""condicionales falsos"""
print(truck == 'WolF'.lower())
"""verdadero porque con el .lower el string es igual al que pusimos en 'truck'"""
print('\n')
 ##condicion de desigualdad != 
print(truck != "ford") #false
print(truck != "wolf") #true
"""desigualdad muentra false porque estamos preguntando si lo que esta en la variable truck es 'ford' y es falso en la variable truck no hay false
               muestra tru porque le preguntamos si lo que etsa en la variable truck es 'wolf' y si es 
"""
print("\n")
 ## comparacion numerica
print("comparaciones numericas")
age=34
print( age==34) #true

answer=17
if answer != 42:
    print("respuesta erronea")

 ## conector menor que <
print("\n conectores <, >, <=, >=".upper())
age=19
print(age < 21) #true
print(age <=21) #true
print(age >21) #false 
print(age >=21) #false
print("\n")

#--------------------------------------------#
# MULTIPLE CONDITION
#--------------------------------------------#
print("\n multiple condition".upper())
age1=22
age2=18
print("operacion and")
print(age1>=21 and age2>=21)#false
print(age1>=21 and age2>=18)#true

print("\n")

print("operacion OR")
print(age1>=21 or age2>=21)

food=["chilaquiles", "flautas", "gorditas", "tamales"]
print("\n nopales esta en la lista?")
print("nopales" in food)
print("\t gorditas esta en la lista?")
print("gorditas" in food)

print("\n")
print("doble negacion")
banned_user=["adrew", "carolina", "david"]
user= "marie"
print(user not in banned_user)#true


