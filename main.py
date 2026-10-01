figura = input("Figura: ")

if figura == "cuadrado":
    lado = float(input("Lado: "))
    area = lado * lado
    print(area)
elif figura == "rectangulo":
    base = float(input("Base: "))
    Altura = float(input("Altura: "))
    print(base * Altura)
elif figura == "triangulo":
    base1 = float(input("Base: "))
    altura = float(input("Altura: "))
    print((base1 * altura)/2)
elif figura == "circulo":
    radio = float(input("Radio: "))
    print(3.1416 * radio * radio)
    