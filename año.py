def calcular_estacion(fecha):
    # Convertir la fecha en una tupla de mes y día
    mes, dia = fecha.split("-")
    mes = int(mes)
    dia = int(dia)

    # Definir los rangos de fechas para cada estación
    primavera = [(3, 21), (6, 20)]
    verano = [(6, 21), (9, 20)]
    otono = [(9, 21), (12, 20)]
    invierno = [(12, 21), (3, 20)]

    if (mes, dia) >= primavera[0] and (mes, dia) <= primavera[1]:
        return "Primavera"
    elif (mes, dia) >= verano[0] and (mes, dia) <= verano[1]:
        return "Verano"
    elif (mes, dia) >= otono[0] and (mes, dia) <= otono[1]:
        return "Otoño"
    else:
        return "Invierno"

def bro():
    try:
        fecha = input("Ingrese la fecha en formato MM-DD: ")
        estacion = calcular_estacion(fecha)
        print("La estación del año para la fecha", fecha, "es:", estacion)

    except ValueError:
        print("Ingrese una fecha válida en el formato especificado.")

if __name__ == "__main__":
    bro()
