def llenar_lista_multiplos_de_7(tamaño):
    lista = [7 * i for i in range(1, tamaño + 1)]
    return lista

def main():
    try:
        tamaño = int(input("Ingrese el tamaño de la lista: "))
        if tamaño <= 0:
            print("El tamaño debe ser un número positivo.")
            return

        lista_multiplos = llenar_lista_multiplos_de_7(tamaño)
        print("Lista de múltiplos de 7:", lista_multiplos)

    except ValueError:
        print("Ingrese un número válido.")

if __name__ == "__main__":
    main()

