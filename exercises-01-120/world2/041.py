birth_year = int(input("\nEnter your date of birth: "))
age = 2026 - birth_year

if age <= 9:
    print("\nChild")

elif age <=14:
    print("\nChildren's")

elif age <=19:
    print("\nJunior")

elif age <= 20:
    print("\nSenior")

else:
    print("\nMaster")