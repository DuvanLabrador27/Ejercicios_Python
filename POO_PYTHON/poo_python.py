class Figura:
    def __init__(self):
        self.lados = None
def main():
    triangulo= Figura()
    cuadrado= Figura()
    rectangulo= Figura()

    triangulo.lados=3
    cuadrado.lados=4
    rectangulo.lados=4


    print(f"El triangulo tiene {triangulo.lados} lados")
    print(f"El cuadrado tiene {cuadrado.lados} lados")
    print(f"El triangulo tiene {rectangulo.lados} lados")
if __name__ == "__main__":
    main()