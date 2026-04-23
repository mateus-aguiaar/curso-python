import random 

aluno1 = str(input("Enter your name: "))
aluno2 = str(input("Enter your name: "))
aluno3 = str(input("Enter your name: "))
aluno4 = str(input("Enter your name: "))

escolhido = [aluno1,aluno2,aluno3,aluno4]
sorteio = random.choice(escolhido)

print(f'The teacher drew the chosen student {sorteio}.')