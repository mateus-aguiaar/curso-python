# Professor quer sortear a ordem dos alunos sorteados para apresentação.
import random

aluno1 = str(input("Digite o seu nome: "))
aluno2 = str(input("Digite o seu nome: "))
aluno3 = str(input("Digite o seu nome: "))
aluno4 = str(input("Digite o seu nome: "))

ordem_sorteio = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(ordem_sorteio)

print(f"A ordem do sorteio foi {ordem_sorteio}.")

