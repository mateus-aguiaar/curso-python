older_man = 0
name_old_man = ""
sum_age = 0
cont_female_minimum = 0
for i in range(1, 5):
    print(f"\n-----{i}# person-----")
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    sex = str(input("Enter your sex [M] OR [F]: "))
    sum_age += age
    if sex == "F" and age < 20:
        cont_female_minimum += 1

    if sex == "M" and i == 1:
        older_man = age
        name_old_man = name

    elif sex == "M" and older_man < age:
        older_man = age
        name_old_man = name

average = sum_age / 4
print(f"\nThe number of women under 20 years old is {cont_female_minimum}.")
print(f"\nThe average age is {average:.2f}")
print(f"\nThe oldest man is {name_old_man} and he is {older_man} years old.")