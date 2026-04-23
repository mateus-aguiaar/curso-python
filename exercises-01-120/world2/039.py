ano_nascimento = int(input("\nEnter your birth year: "))
tempo_atraso = 2008 - ano_nascimento
tempo_falta = ano_nascimento - 2008

if ano_nascimento > 2008:
    print(f"You will still enlist.\n{tempo_falta} year(s) left.")

elif ano_nascimento == 2008:
    print("It is time to enlist.")

else:
    print(f"\nThe enlistment period has already passed.\nPassed by {tempo_atraso} year(s).")