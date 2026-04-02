# Progama para deixar a frase em maiúsculo e minúsculo, contar as letras do nome sem considerar os espaços e descobrir quantas letras tem o primeiro nome.
nome = input(str('Digite o seu nome: '))

print(nome.upper())

print(nome.lower())

print(len(nome.replace(' ', '')))

print(len(nome.split()[0]))