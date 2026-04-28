exit = 0
first_number = float(input("\nEnter the first value: "))
second_number = float(input("\nEnter the second value: "))
while exit < 1:
    print("\n[1] - add\n[2] - multiply\n[3] - greater\n[4] - new numbers\n[5] - exit the program")
    option = int(input("\nEnter the desired option: "))

    if option == 1:
        print(f"\nThe sum of {first_number} + {second_number} is equal to {first_number + second_number}.")

    elif option == 2:
        print(f"\nThe multiplication of {first_number} and {second_number} is equal to {first_number * second_number}.")

    elif option == 3:
        if first_number > second_number:
            print("\nThe first value is greater.")
        elif second_number > first_number:
            print("\nThe second value is greater.")
        else:
            print("\nThe numbers are equal.")

    elif option == 4:
        print("\nEnter the new values.")
        first_number = float(input("\nEnter the first value: "))
        second_number = float(input("\nEnter the second value: "))

    elif option == 5:
        exit += 1
        
    else:
        print("\nInvalid option")
print("\nProgram finished.")