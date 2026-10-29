"""programa que calcule el total de una cuenta o un 
tiket tomando en cuenta el Iva y la propina"""

subtotal_txt=input("subtotal (MXN): ")
iva_txt=input("iva (%) ejemplo 16: ")
tip_txt=input("propina (%) ej: 10: () ")

try:
    subtotal=float(subtotal_txt)
    iva=float(iva_txt)/100
    tip=float(tip_txt)/100
except:
    print("entrada no valida")
    raise SystemExit(1)

iva_acount=subtotal*iva
tip_acount=subtotal*tip
total=subtotal+iva_acount+tip_acount

print("subtotal", subtotal)
print("iva", iva )
print("tip", tip)

