class Persona():

    def __init__(self,nombre,cargo):
        self.__nombre = nombre
 
        self.__cargo = cargo
    
    def  get_nombre(self):
        return self.__nombre
    
    def get_cargo(self):
        return self.__cargo
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def set_cargo(self,cargo):
        self.__cargo = cargo

    def __str__(self):
        return str(self.__nombre) + "," +  str(self.__cargo)

class Frestayler(Persona):
    def __init__(self,nombre,cargo,apodo,habilidad):
        super().__init__(nombre,cargo)
        self.__apodo=apodo
        self.__habilidad=habilidad
    
    def get_apodo(self):
        return self.__apodo

    def set_apodo(self,apodo):
            self.__apodo = apodo
    
    def get_habilidad(self):
        return self.__habilidad

    def set_habilidad(self,habilidad):
        self.__habilidad = habilidad

    def __str__(self):
        return str(self.__apodo) + "," +  str(self.__habilidad)

class Fms(Frestayler):
    def __init__(self,nombre,cargo,apodo,habilidad,nombreFms,cantidadCompetidores):
        super().__init__(nombre,cargo,apodo,habilidad)
        self.__nombreFms=nombreFms
        self.__cantidadCompetidores=cantidadCompetidores
    
    def  get_nombreFms(self):
            return self.__nombreFms
    
    def get_cantidadCompetidores(self):
        return self.__cantidadCompetidores
    
    def set_nombreFms(self,nombreFms):
        self.__nombreFms = nombreFms
    
    def set_cantidadCompetidores(self,cantidadCompetidores):
        self.__cantidadCompetidores = cantidadCompetidores
    
    def __str__(self):
         return str(self.__nombreFms) + "," +  str(self.__cantidadCompetidores)
    
participante=Fms("Mau","Frestayler","Aczino","Punchline","Fms Mexico",12)
print("""
Hola {0} tu apodo es {1}, eres un {2}, tu habilidad es {3}, estas en la {4} y hay {5} competidores

 """.format(participante.get_nombre(), participante.get_apodo(), participante.get_cargo(), participante.get_habilidad(),participante.get_nombreFms(), participante.get_cantidadCompetidores()))


    

