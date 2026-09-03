Seleccion = []

while True:
    Tam = int(input("¿De qué tamaño quiere su cuadrícula? (Debe ser mayor o igual a 8): "))

    if Tam >= 8:
        break
    else:
        print("El tamaño ingresado es inválido, recuerde que el tamaño de su cuadrícula debe ser mayor o igual a 8")


def Vista_cuadric():
    print("\n  ", end="")

    for x in range(1, Tam + 1):
        print(x, end=" ")

    print()

    for y in range(1, Tam + 1):
        print(y, end=" ")

        for x in range(1, Tam + 1):
            if (x, y) in Seleccion:
                print("•", end=" ")
            else:
                print("○", end=" ")

        print()


def selec_coord():
    x = int(input("Ingresa la coordenada en X: "))
    y = int(input("Ingrese la coordenada en Y: "))

    if x >= 1 and x <= Tam and y >= 1 and y <= Tam:
        if (x, y) not in Seleccion:
            Seleccion.append((x, y))
            print("La coordenada seleccionada es", (x, y))
        else:
            print("Esa coordenada ya fue seleccionada")
    else:
        print("Coordenada inválida, esta debe estar entre 1 y", Tam)


def reiniciar():
    Seleccion.clear()
    print("Se reinició la cuadrícula")


while True:
    Vista_cuadric()

    print("\n1. Seleccionar coordenadas")
    print("2. Reiniciar")
    print("3. Salir")

    opcion = input("Seleccione una opción (selecciona el número): ")

    if opcion == "1":
        selec_coord()

    elif opcion == "2":
        reiniciar()

    elif opcion == "3":
        print("El programa se ha finalizado")
        break

    else:
        print("Opción inválida")
        