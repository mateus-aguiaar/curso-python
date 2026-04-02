nome = str(input('Digite o seu nome: ')).split()

print(f'\033[1;34mO primeiro nome é {nome[0]}\033[m')
print(f'\033[1;35mO ultimo nome é {nome[-1]}\033[m')