import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base,altura):
    return base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base,altura):
    return (base * altura) / 2

def mostrar_resultado(figura,area):
    print(f"El area del{figura} es: {area:.2f}")

def main():
    mostrar_resultado(
        "cuadrado",
        calcular_area_cuadrado(5)
    )
    mostrar_resultado(
            "rectangulo",
            calcular_area_rectangulo(5,3)
        )
    mostrar_resultado(
            "circulo",
            calcular_area_circulo(4)
        )
    mostrar_resultado(
            "triangulo",
            calcular_area_triangulo(10,5)
        )

if __name__== "__main__":
    main()