# Progama leia o comprimento do cateto oposto e do cateto adjacente e calcule o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(f"Um triângulo retangulo de cateto oposto igual a {cateto_oposto} e cateto adjacente igual a {cateto_adjacente}, tem a sua hipotenusa igual a {(hipotenusa):.2f} ")