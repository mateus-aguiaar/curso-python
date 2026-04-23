import random

aluno1 = str(input("Enter your name: "))
aluno2 = str(input("Enter your name: "))
aluno3 = str(input("Enter your name: "))
aluno4 = str(input("Enter your name: "))

ordem_sorteio = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(ordem_sorteio)

print(f"The order of the draw was {ordem_sorteio}.")