nombres=[]
Carnet=[]
n=5
for x in range(n):
    nom=input("Ingrese su/s nombre/s y apellido/s:")
    nombres.append(nom)
    Carn=int(input("Ingrese su num de Carnet:"))
    Carnet.append(Carn)
for k in range(n-1):
    for x in range((n-1)-k):
        if nombres[x]>nombres[x+1]:
            aux=nombres[x]
            nombres[x]=nombres[x+1]
            nombres[x+1]=aux
            aux2=Carnet[x]
            Carnet[x]=Carnet[x+1]
            Carnet[x+1]=aux2
print("listado en orden")
for x in range(n):
    print(nombres[x],Carnet[x])