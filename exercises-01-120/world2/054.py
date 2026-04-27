from datetime import date
current_year = date.today().year
cont_high = 0
cont_minor = 0

for i in range(7):
    birth_year = int(input("\nEnter your date of birth: "))
    if current_year - birth_year >= 18:
        cont_high += 1
    else:
        cont_minor += 1

print(f"\nThe total number of people over 18 years old is {cont_high}.")
print(f"\nThe total number of people under 18 years old is {cont_minor}.")