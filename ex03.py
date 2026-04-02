# Média do aluno:
nome_Do_Aluno = input("\nDigite o seu nome: ")
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("\nDigite a segunda nota: "))

cal_media = (n1 + n2) / 2

print("A média do aluno {} foi {:.1f}".format(nome_Do_Aluno,cal_media))