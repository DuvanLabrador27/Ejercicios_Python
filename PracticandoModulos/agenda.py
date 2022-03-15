from operator import truediv
import os
SALIR=0
AGREGAR=1
MOSTRAR=2
BUSCAR=3
MODIFICAR=4
ELIMINAR=5

def mostrarMenu():
    
    print(
        """
        {AGREGAR}) Agregar
        {MOSTRAR}) Mostrar 
        {BUSCAR}) Buscar
        {MODIFICAR}) Modificar
        {SALIR}) Salir

        """
    )

def agregarContactos(agenda):
   
    print("       Add a contact")
    nombre=input("Ingrese el nombre: ")
    if agenda.get(nombre):
        print("Ups! este contacto ya existe!!")
    else:
        print("Registrate!!")
        telefono=input("Ingrese el telefono: ")
        email=input("Ingrese el email: ")
        agenda.setdefault(nombre,(telefono,email))
        print("Contacto agg con éxito!!!")
def mostrarContacto(agenda):
    
    print("Mis contactos")
    if len(agenda)>0:
        for contacto, datos in agenda.items():
           print(f"Nombre: {contacto}")
           print(f"Telefono: {datos[0]}")
           print(f"email: {datos[1]}")
           print("---------------------------")

    else:
        print("No tienes contactos!!")

def main():
    continuar=True
    mi_agenda={}
    while continuar:
        mostrarMenu()
        opc=int(input("Ingrese una opcion: "))
        if opc==AGREGAR:
            agregarContactos(mi_agenda)
        elif opc==MOSTRAR:
            mostrarContacto(mi_agenda)
        elif opc==SALIR:
            continuar=False
            print("Gracias por agg contactos")
        else:
            print("Opcion incorrecta")

if __name__=='__main__':
    main()