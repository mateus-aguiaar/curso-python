n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
menor = n1
if n2 < n1 and n3:
    menor = n2

if n3 < n1 and n2:
    menor = n3

print(f'O menor valor é {menor}')

maior = n1

if n2 > n1 and n3:
    maior = n2

if n3 > n1 and n2:
    maior = n3

print(f'O maior valor é {maior}')



