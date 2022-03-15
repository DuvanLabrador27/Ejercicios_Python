def CalcularFactorial():
    numero_a_calcular=int(input("Ingrese el número: "))
    factorial=1
    for i in range(1,(numero_a_calcular+1)):
        factorial=factorial*i
    print("El factorial de {0} es: {1}".format(numero_a_calcular,factorial))
CalcularFactorial()