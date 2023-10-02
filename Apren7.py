alt=0
baj=0
x=1
while x<=10:
    nota=int(input("ingrese una nota:"))
    if nota>=7:
        alt=alt+1
    else:
        baj=baj+1
    x=x+1
print("notas altas")
print(alt) 
print("notas bajas")
print(baj)