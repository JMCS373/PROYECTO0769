nombres=[]
n=5
for x in range(n):
    nom=input("Ingrese su/s nombre/s y apellido/s:")
    nombres.append(nom)
nombrL=nombres[0]
for x in range(1,5):
    if nombres[x]<nombrL:
        nombrL=nombres[x]
print("Nombre menor")
print(nombrL)
print("Lista de nombres:")
print(nombres)