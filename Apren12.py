"""variable.Upper()=Mayusculas
variable.lower()=minusculas
variable.capitalize()=primera Mayuscula
len(variable)=largo de la cadena
Nuevavariable.append(variable)=toma valores tipo lista
"""
N=[]
for x in range(5):
    L=float(input("ingrese el valor:"))
    N.append(L)
mayor=N[0]
for x in range(1,5):
    if N[x]>mayor:
        mayor=N[x]
print(N)
print(mayor)
