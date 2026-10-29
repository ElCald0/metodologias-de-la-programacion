"""
calcular imc
peso
altura

"""
weight_txt=input("peso (kg): ")
height_txt=input("altura mts: ")
try:
    weight=float(weight_txt)
    height=float(height_txt)
    imc=weight/(height**2)
    print(f"tu imc es :{imc}")
except:
    print("datos no validos, la altura debe ser dsitinta a cero")








