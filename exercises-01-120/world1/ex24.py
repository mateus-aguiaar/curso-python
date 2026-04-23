nome = str(input('Enter your name: ')).split()

print(f'\033[1;34mThe first name is {nome[0]}\033[m')
print(f'\033[1;35mThe last name is {nome[-1]}\033[m')