""" 
Utilice el programa anterior (2.2) para generar una tabla de conversión de temperaturas,
desde 0 °F hasta 120 °F, de 10 en 10.
"""

print("----------------------------------------------")
print("TABLA DE CONVERSIÓN DE TEMPERATURAS")

for grados_f in range(0,121,10):
    grados_c = (grados_f - 32 ) * 5/9
    print(f" {grados_f:.2f}º F son {grados_c:.2f}º C")
