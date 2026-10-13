"""
ejercicio:
hacer un prohgrama que determine el costo de un boleto a partir de las siguientes condiciones

-costo para una persona menor o igual a 4 anos: gratis
-costo para una persona cuya edad es mayor a 4 años pero menor o igual de 18: $200
-costo para persona mayor a 18: $500
"""
age=2
if age <=4:
    cost=0
if age>4 and age <=18:
    cost=400
if age>18:
    cost=500
print(f"el costo de tu boleto es:{cost}")

##if elif else
