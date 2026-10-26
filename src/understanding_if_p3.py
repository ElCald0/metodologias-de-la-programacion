guisos=["salsa verde","deshebrada","nopalitos del cerrito"]

if "salsa verde" in guisos:
    print("hay salsa verde disponible")

elif "deshebrada" in guisos:
    print("hay deshebrada disponible")

elif "guiso especial" in guisos:
    print("hay guiso especial disponible")

#-------------------------------------#
## lista vacia
#-------------------------------------#
guisos_revenge=[]
if guisos_revenge:
    for guiso in guisos_revenge:
        print(guiso)
else:
    print("no hay")

print("\n")
#---------------------------------------------#
## 
#---------------------------------------------#
guisos_disponibes=["salsa verde", "deshebrada", "picadillo", "asado"]
guisos_a_ordenar=["barbacoa", "deshebrada", "cabrito"]

for guiso in guisos_a_ordenar:
    if guisos in guisos_disponibes:
        print("si hay de se guiso")
else:
    print("una disculpa no tenemos ese guiso")






