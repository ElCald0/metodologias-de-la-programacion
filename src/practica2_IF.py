"""
ejercicio:
hacer un prohgrama que determine el costo de un boleto a partir de las siguientes condiciones

-costo para una persona menor o igual a 4 anos: gratis
-costo para una persona cuya edad es mayor a 4 años pero menor o igual de 18: $200
-costo para persona mayor a 18: $500
"""
print("esto se hace con el if normal \n")
age=67
if age <=4:
    cost=0
if age>4 and age <=18:
    cost=400
if age>18:
    cost=500
print(f"el costo de tu boleto es:{cost}")
print("\n")

#---------------------------------------------------------------------#
##if-elif-else
#---------------------------------------------------------------------#

print("esto se hace con el if-elif-else \n".upper())

if age <=4:
    cost=0
elif age>4 and age <18:
    cost=400
elif age>=18 and age <65:
    cost=500
elif age >=65:
    cost=0
#else:
 #   cost=1    #
print(f"el costo de tu boleto es:{cost}")



























