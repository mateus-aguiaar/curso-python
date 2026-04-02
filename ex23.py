import random

num = random.randint(1,5)
escolha = int(input('Digite a sua escolha de número de 1 a 5: '))

if escolha == num:
    print('O usuário venceu!')

else:
    print('O usuário perdeu.')

print(f'O valor sorteado é {num}')