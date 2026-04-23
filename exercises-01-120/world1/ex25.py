import random

num = random.randint(1,5)
escolha = int(input('Enter your number choice from 1 to 5: '))

if escolha == num:
    print('The user won!')

else:
    print('The user lost.')

print(f'The drawn value is {num}')