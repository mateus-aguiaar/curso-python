from datetime import date
atual = date.today().year
birth_year = int(input("\nEnter your date of birth: "))
age = atual - birth_year

if age <= 9:
    print("\nClassification: Child")

elif age <=14:
    print("\nClassification: Children's")

elif age <=19:
    print("\nClassification: Junior")

elif age <= 25:
    print("\nClassification: Senior")

else:
    print("\nClassification: Master")