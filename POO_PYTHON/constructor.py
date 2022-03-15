#Creamos una clase
class Curso():
    #Declaramos variables
    """
    nombre="Matematicas"
    creditos=5
    profesion="Ingenieria de sistemas"
    """
    def  __init__(self, nombre, creditos, profesion):
        self.nombre =nombre
        self.creditos=creditos
        self.profesion=profesion

#Instanciamos el objeto 
curso=Curso("Matematicas",3,"Ingenieria de sistemas")
print("El nombre del curso es {0}".format(curso.nombre))
print("El numero de creditos es {0}".format(curso.creditos))
print("El nombre de la profesion es {0}".format(curso.profesion))
curso2=Curso("POO",4,"Ingenieria de sistemas")
print("El nombre del curso es {0}".format(curso2.nombre))
print("El numero de creditos es {0}".format(curso2.creditos))
print("El nombre del la profesion es {0}".format(curso2.profesion))