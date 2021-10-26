# Media, mediana y varianza

num1 = float(input("Escribe el número 1: "))
num2 = float(input("Escribe el número 2: "))
num3 = float(input("Escribe el número 3: "))

lista = [num1, num2, num3]
def mean(datos):
    return sum(datos) / len(datos)

print("Media de la lista: ", mean(lista))

def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StadisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2

print("Mediana: ", median(lista))

import numpy
varianza = numpy.var(lista)
print("Varianza: ", varianza)