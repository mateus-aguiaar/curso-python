n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))
menor = n1
if n2 < n1 and n3:
    menor = n2

if n3 < n1 and n2:
    menor = n3

print(f'The smallest value is {menor}')

maior = n1

if n2 > n1 and n3:
    maior = n2

if n3 > n1 and n2:
    maior = n3

print(f'The largest value is {maior}')