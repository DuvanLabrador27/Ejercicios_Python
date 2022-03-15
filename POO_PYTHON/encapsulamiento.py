class encapsulamiento():

    def  __init__(self, propietario, saldo, moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda

        #Getters

    def get_saldo(self):
        return self.__saldo

    def get_propietario(self):
        return self.__propietario

    def get_moneda(self):
        return self.__moneda

        #Setters

    def set_saldo(self,saldo):
        self.__saldo= saldo

    def set_propietario(self, propietario):
        self.__propietario= propietario
    
    def set_moneda(self, moneda):
        self.__moneda= moneda

cuenta=encapsulamiento("Duvan",15000,"USD")
print("Señor {0}, usted tiene {1} {2} en su cuenta, muchas gracias por consultar".format(cuenta.get_propietario(), cuenta.get_saldo(), cuenta.get_moneda()))
cuenta.set_moneda("EUR")
print("---------------------------------------------------------------------------------------")
print("Señor {0}, usted tiene {1} {2} en su cuenta, muchas gracias por consultar".format(cuenta.get_propietario(), cuenta.get_saldo(), cuenta.get_moneda()))