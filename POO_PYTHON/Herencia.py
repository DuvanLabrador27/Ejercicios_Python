class Persona():
    def  __init__(self,nombre,apellido,identificacion):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__identificacion=identificacion

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_identificacion(self):
        return self.__identificacion
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def set_apellido(self,apellido):
        self.__apellido=apellido
    
    def set__identificacion(self,identificacion):
        self.__identificacion=identificacion
    
    def __str__(self):
        return str(self.__nombre) + "," + str(self.__apellido) + "," + str(self.__identificacion)

class Estudiante(Persona):
    def __init__(self,nombre,apellido,identificacion,profesion):
        super().__init__(nombre,apellido,identificacion)
        self.__profesion=profesion  

    def get_profesion(self):
        return self.__profesion
    
    def set_profesion(self,profesion):
        self.__profesion=profesion

    def __str__(self):
        return str(self.__profesion)

persona=Persona("Duvan","Labrador",115)
estudiante=Estudiante("Duvan", "Labrador",1151808,"Ingenieria de sistemas")
print(persona)
print("-------------")
print("Hola {0} {1}, tu codigo es {2} y tu profesion es {3} ".format(estudiante.get_nombre(), estudiante.get_apellido(), estudiante.get_identificacion(), estudiante.get_profesion()))


