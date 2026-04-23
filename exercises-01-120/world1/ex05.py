nome_Do_Aluno = input("\nEnter your name: ")
n1 = float(input("\nEnter the first grade: "))
n2 = float(input("\nEnter the second grade: "))

cal_media = (n1 + n2) / 2

print("The student {}'s average was {:.1f}".format(nome_Do_Aluno,cal_media))