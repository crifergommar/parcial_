import pandas as pd
from pandas import ExcelWriter

consultar=""
nombre=[]
apellido=[]
edad=[]
sexo=[]
celular=[]
while consultar != "N":
    nuevo_nombre=input("Ingrese su nombre: ")
    nombre.append(nuevo_nombre)
    
    nuevo_apellido=input("Ingrese su apellido: ")
    apellido.append(nuevo_apellido)

    nuevo_cedula=input("Ingrese su N° de Cedula: ")
    edad.append(nuevo_cedula)

    print("Casa o Apartamento? \n")
    nuevo_tipo=input("Ingrese el tipo de vivienda: ")
    nombre.append(nuevo_tipo)

    nuevo_numerocasa=input("Ingrese el numero de ",nuevo_tipo, " : ")
    nombre.append(nuevo_numerocasa)

    nuevo_telefono=input("Ingrese su telefono : ")
    nombre.append(nuevo_telefono)

    nuevo_correo=input("Ingrese su correo electronico : ")
    nombre.append(nuevo_correo)