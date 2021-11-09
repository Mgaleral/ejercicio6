# Media, mediana y varianza

import statistics

n1 = int(input("Introduzca el primer dato numérico: "))
n2 = int(input("Introduzca el segundo dato numérico: "))
n3 = int(input("Introduzca el tercer dato numérico: "))

n = [n1, n2, n3]

media = statistics.mean(n)
mediana = statistics.median(n)
varianza = statistics.variance(n)

print("Media: ", media)
print("Mediana: ", mediana)
print("Varianza: ", varianza)
