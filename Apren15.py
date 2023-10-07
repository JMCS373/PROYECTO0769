#LIBRERIAS DEL PROGRAMA
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import messagebox as mb

# PROGRAMA TIPO APLICACION
class ACADEMIA:
    
    #VENTANA DE INICIO
    def __init__(self):

        self.ventana1=tk.Tk()
        fuente_personalizada = tkFont.Font(family="Arial", size=16, weight="bold")
        fuente_personalizada2 = tkFont.Font(family="Arial", size=10, weight="bold")
        self.canvas1=tk.Canvas(self.ventana1, width=200, height=200)
        self.canvas1.grid(column=1, row=0)
        archi1=tk.PhotoImage(file="ASDF.png")
        self.canvas1.create_image(25,0, image=archi1, anchor="nw")
        self.ventana1.title("ACADEMIA USAC")
        self.label1=tk.Label(self.ventana1, text=" INICIAR COMO:", font=fuente_personalizada)
        self.label1.grid(column=1, row=5, padx=5, pady=5)

        # BOTON DE REGISTRO COMO ESTUDIANTE 

        self.Boton1=tk.Button(self.ventana1, text="REGISTRO ESTUDIANTE", font=fuente_personalizada2, command=self.Ingreso)
        self.Boton1.grid(column=1, row=10, padx=5, pady=5)

        # BOTON DE INICIO COMO ESTUDIANTE 

        self.Boton2=tk.Button(self.ventana1, text="ESTUDIANTE", font=fuente_personalizada2, command=self.EstudianteUSAC)
        self.Boton2.grid(column=1, row=15, padx=5, pady=5)

        # BOTON DE INICIO COMO CATEDRATICO

        self.Boton3=tk.Button(self.ventana1, text="CATEDRATICO", font=fuente_personalizada2)#, command=self.CatedraticoUSAC)
        self.Boton3.grid(column=1, row=20, padx=5, pady=5)
        
        # BOTON DE INICIO COMO ADMINISTRADOR
        
        self.Boton4=tk.Button(self.ventana1, text="ADMINISTRADOR", font=fuente_personalizada2)#, command=self.AdminUSAC)
        self.Boton4.grid(column=1, row=25, padx=5, pady=5)
        self.ventana1.mainloop()
#-----------------------------------------------------------------------------------------------------------
    #REGISTRO DEL ESTUDIANTE
    def Ingreso(self):

        #REGISTRO DE ESTUDIANTES, CATEDRATICOS, ADMINISTRADOR
        #archi1=open("REGISTROS.txt","w")

        #VENTANA DE ESTUDIANTES
        self.ventana1=tk.Tk()
        self.ventana1.title("INGRESO COMO ESTUDIANTE:")
        fuente_personalizada = tkFont.Font(family="Arial", size=10, weight="bold")
        #INGRESO DE CREDENCIALES DEL ESTUDIANTE
        #NOMBRE
        self.Name=tk.Label(self.ventana1, text="Ingrese su/s nombre/s", font=fuente_personalizada)
        self.Name.grid(column=0, row=4)
        self.Nombre=tk.StringVar()
        Entry1=ttk.Entry(self.ventana1, width=50, textvariable=self.Nombre)
        Entry1.grid(column=0, row=10)
        #archi1.write(self.Nombre)
        #APELLIDOS
        self.LName=tk.Label(self.ventana1, text="Ingrese su/s apellidos/s", font=fuente_personalizada)
        self.LName.grid(column=1, row=4)
        self.LNombre=tk.StringVar()
        Entry2=ttk.Entry(self.ventana1, width=50, textvariable=self.LNombre)
        Entry2.grid(column=1, row=10, padx=5, pady=5)
        #DPI
        self.DPI=tk.Label(self.ventana1, text="Ingrese su DPI", font=fuente_personalizada)
        self.DPI.grid(column=2, row=4)
        self.DPIs=tk.StringVar()
        Entry3=ttk.Entry(self.ventana1, width=50, textvariable=self.DPIs)
        Entry3.grid(column=2, row=10)
        #FECHA DE NACIMIENTO
        self.FNA=tk.Label(self.ventana1, text="Ingrese su fecha de nacimiento", font=fuente_personalizada)
        self.FNA.grid(column=0, row=14)
        self.FNAs=tk.StringVar()
        Entry4=ttk.Entry(self.ventana1, width=50, textvariable=self.FNAs)
        Entry4.grid(column=0, row=20)
        #TELEFONO
        self.PHON=tk.Label(self.ventana1, text="Ingrese su numero de telefono", font=fuente_personalizada)
        self.PHON.grid(column=1, row=14)
        self.PHONs=tk.StringVar()
        Entry5=ttk.Entry(self.ventana1, width=30, textvariable=self.PHONs)
        Entry5.grid(column=1, row=20)
        #NOMBRE DE USUARIO
        self.USER=tk.Label(self.ventana1, text="Ingrese su nombre de usuario", font=fuente_personalizada)
        self.USER.grid(column=2, row=14)
        self.USERs=tk.StringVar()
        Entry6=ttk.Entry(self.ventana1, width=20, textvariable=self.USERs)
        Entry6.grid(column=2, row=20)
        #CORREO ELECTRONICO
        self.email=tk.Label(self.ventana1, text="Ingrese su Correo Electronico", font=fuente_personalizada)
        self.email.grid(column=0, row=24)
        self.emails=tk.StringVar()
        Entry7=ttk.Entry(self.ventana1, width=50, textvariable=self.emails)
        Entry7.grid(column=0, row=30)
        #CONTRASEÑA
        self.CONTRA=tk.Label(self.ventana1, text="Ingrese su Contraseña", font=fuente_personalizada)
        self.CONTRA.grid(column=1, row=24)
        self.CONTRAS=tk.StringVar()
        Entry8=ttk.Entry(self.ventana1, width=20, textvariable=self.CONTRAS, show="*")
        Entry8.grid(column=1, row=30)
        #CONFIRMAR CONTRASEÑA
        self.CONTRA2=tk.Label(self.ventana1, text="Vuelva a ingresar su Contraseña", font=fuente_personalizada)
        self.CONTRA2.grid(column=2, row=24)
        self.CONTRAS2=tk.StringVar()
        Entry9=ttk.Entry(self.ventana1, width=20, textvariable=self.CONTRAS2, show="*")
        Entry9.grid(column=2, row=30, padx=5, pady=5)
        #BOTON DE REGISTRAR
        self.Boton=tk.Button(self.ventana1, text="REGISTRAR USUARIO", font=fuente_personalizada, command=self.COMPROBACION)
        self.Boton.grid(column=1, row=40)
#----------------------------------------------------------------------------------------------------------
        #COMPROBACION DE DATOS INGRESADOS
    def COMPROBACION(self):
        
        #global nombre 
        nombre = self.Nombre.get()
        #global apellido
        apellido = self.LNombre.get()
        #global DPI
        DPI = self.DPIs.get()
        #global FN
        FN = self.FNAs.get()
        #global tel
        tel = self.PHONs.get()
        #global NS
        NS = self.USERs.get()
        #global Email
        Email = self.emails.get()
        #global Con
        Con = self.CONTRAS.get()
        #global Cons
        Cons = self.CONTRAS2.get()
        print(nombre)
        if nombre=="" or apellido=="" or DPI=="" or FN=="" or tel=="" or NS=="" or Email=="" or Con=="" or Cons=="":
            mb.showerror("ALERTA","DATOS FALTANTES")
        if Con != Cons:
            mb.showerror("ALERTA","LA CONTRASEÑA NO ES IGUAL")
        #else:
            #self.VENTANAEST()
#----------------------------------------------------------------------------------------------------------
    #INICIO DE SESION COMO ESTUDIANTE
    def EstudianteUSAC(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("INGRESO COMO ESTUDIANTE:")
        #NOMBRE DE USUARIO
        self.USERI=tk.Label(self.ventana1, text="Ingrese su usuario")
        self.USERI.grid(column=0, row=5)
        self.USERIS=tk.StringVar()
        Entry10=tk.Entry(self.ventana1, width=20, textvariable=self.USERIS)
        Entry10.grid(column=0, row=10)
        #CONTRASEÑA
        self.CONTRAI=tk.Label(self.ventana1, text="Ingrese la contraseña")
        self.CONTRAI.grid(column=2, row=5)
        self.CONTRAIS=tk.StringVar()
        Entry11=tk.Entry(self.ventana1, width=20, textvariable=self.CONTRAIS, show="*")
        Entry11.grid(column=2, row=10)
        #BOTON PARA INGRESAR
        self.Boton=tk.Button(self.ventana1, text="INGRESAR", command=COMPROBACION2)
        self.Boton.grid(column=4, row=10)
#----------------------------------------------------------------------------------------------------------
        #COMPROBACION INICIO DE SESION ESTUDIANTE
        def COMPROBACION2(self):
            US = Entry10.get()
            Con = Entry11.get()
            if US()=="" or Con()=="":
                mb.showerror("ALERTA","DATOS FALTANTES")
            else:
                self.VENTANAEST() 
#----------------------------------------------------------------------------------------------------------
    #VENTANA PRINCIPAL ESTUDIANTE
    def VENTANAEST():
        print("HOLA")
#----------------------------------------------------------------------------------------------------------        

#BLOQUE MADRE
ACADEMIAUSAC =ACADEMIA()


#CHECK BUTTON
#self.seleccionN=tk.IntVar()
#self.check1=ttk.Checkbutton(self.ventanaN, text="Python", variable=self.seleccionN)
#self.check1.grid(column=N, row=N)

#CUADERNILLO ESTUDIANTE
#self.cuaderno1=ttk.Notebook(self.ventanaN)
#self.pagina1=ttk.Frame(self.cuaderno1)
#LOS DEMAS SELF, LLEVAN EL NUMERO DE CUADERNO