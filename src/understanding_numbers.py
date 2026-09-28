#           NUMEROS
# ENTEROS - Integers

"""
los numeros enteros se pueden sumar (+), restar (-), multiplicar (*), 
y dividir (/), dividir enteros (//), residu de la divisione(4%2), potencias(**n)(3**2)

"""

print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3**2)

age = 18
name = "caldow"

print(name, age)


# FLOATS    
"""python floats son cualquier numero con punto decimal"""
print(0.2+0.2)
print (0.2-0.3)
print(0.2*0.4)

age = 18 ##variable tipo entero

## message = "caldo tiene" + age +"años."

## print(message)
"""
TYPE ERROR: python no puede reconocer el 
tipo de informacion que se esta utilizando
En este caso no se puede concatenar ints a strings
"""
message = "caldo tiene " + str(age) +" años."
print(message)
message_f = f"caldo tiene {age} años."

print(message)
print(type(age))
print(type(0.1))
print(type(message))



