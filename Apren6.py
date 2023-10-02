x=1 
cant=0
n=int(input("ingrese cuantas piezas va a procesar:"))
while x<=n:
    largo=float(input("ingresar medida de la pieza:"))
    if largo>1.20 and largo<1.30:
        cant=cant+1
    x=x+1
print("Cantidad de piezas aptas")
print(cant) 