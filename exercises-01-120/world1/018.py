from math import cos, tan, sin, radians

angulo = int(input('Enter an angle: '))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'\033[1;34mThe angle has a sine equal to {seno:.2f} \nCosine equal to {cosseno:.2f}  \nTangent equal to {tangente:.2f}\033[m ')