"""Una empresa tiene dos turnos, en los que trabajan 8 empleados, 4 y 4, 
programa que permite almacenar los sueldos de los empleados agrupados en dos listas """
Msueldo=[]
Nsueldo=[]
print("sueldos del turno de mañana:")
for x in range(4):
    sueldo=float(input("ingrese el sueldo:"))
    Msueldo.append(sueldo)
print("sueldos del turno de tarde:")
for x in range(4):
    sueldo=float(input("ingrese el sueldo:"))
    Nsueldo.append(sueldo)
print("SUELDOS DE MAÑANA:")
print(Msueldo)
print("SUELDOS DE TARDE:")
print(Nsueldo)