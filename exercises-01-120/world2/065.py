quantity_values = 0
accumulator = 0
option = 0
highest_initial = 0
lowest_initial = 0

while option != 2:
    numbers = int(input("\nEnter a value: "))
    quantity_values += 1
    if quantity_values == 1:
        highest_initial = numbers
        lowest_initial = numbers
    accumulator += numbers
    print("\n[1] - Add more a value\n[2] - End the program")
    option = int(input("Enter a option: "))
    if quantity_values > 1:
        if numbers > highest_initial:
            highest_initial = numbers

        elif numbers < lowest_initial:
            lowest_initial = numbers

average = accumulator / quantity_values
print(f"\nThe average of the values is equal to {average}.")
print(f"\nThe highest value was {highest_initial} and the lowest {lowest_initial}.")