people_over18 = 0
men_count = 0
women_under20 = 0
while True:
    try:
        age = int(input("\nEnter your age: "))
    except ValueError:
        print("Invalid age! Please enter a number.")
        continue

    while True:
        gender = input("Enter your gender, [M] or [F]: ").upper().strip()
        if gender in ("M", "F"):
            break
        print("Invalid gender! Please enter M or F.")

    print("\033[1;32mRegistration completed!\033[m")
    print("\n[1] - Continue\n[2] - Exit")
    option = int(input("Choose an option: "))

    if age >= 18:
        people_over18 += 1

    if gender == "M":
        men_count += 1

    if gender == "F" and age < 20:
        women_under20 += 1

    if option == 1:
        continue
    elif option == 2:
        break

print(f"\nPeople over 18: {people_over18}")
print(f"\nMen registered: {men_count}")
print(f"\nWomen under 20: {women_under20}")