# Calcular o seno,cosseno e tangente de um ângulo.
from math import cos, tan, sin, radians

angulo = int(input('Digite um ângulo: '))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'\033[1;34mO ângulo tem o seno igual a {seno:.2f} \nCosseno igual a {cosseno:.2f}  \nTangente igual a {tangente:.2f}\033[m ')