# progamo ler um número real e mostrar a parte inteira.
from math import trunc
num = float(input("Digite um número: "))
num_inteiro = trunc(num)

print(f"A parte inteira desse número {(num):.2f} é {num_inteiro}")

## Poderia usar o int no lugar do trunc.