# Sorteio de alunos para apagar o quadro.
import random 

aluno1 = str(input("Digite o seu nome: "))
aluno2 = str(input("Digite o seu nome: "))
aluno3 = str(input("Digite o seu nome: "))
aluno4 = str(input("Digite o seu nome: "))

escolhido = [aluno1,aluno2,aluno3,aluno4]
sorteio = random.choice(escolhido)

print(f'O professor sorteou o aluno escolhido {sorteio}.')