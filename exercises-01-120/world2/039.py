from datetime import date
atual = date.today().year
ano_nascimento = int(input("\nEnter your birth year: "))
idade =  atual - ano_nascimento
tempo_falta = 18 - idade
tempo_atraso = idade - 18

if idade < 18:
    print(f"\nYou will still enlist.\n{tempo_falta} year(s) left.")

elif ano_nascimento == 18:
    print("\nIt is time to enlist.")

else:
    print(f"\nThe enlistment period has already passed.\nPassed by {tempo_atraso} year(s).") 