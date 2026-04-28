quantity_numbers = 0
accumulator = 0
number = 0
while number != 999:
    number = int(input("\nEnter the value: "))
    if number != 999:
        quantity_numbers += 1
        accumulator += number
    else:
        print("\nEnd of program")
print(f"\nThe quantity of numbers entered was {quantity_numbers} and the sum was {accumulator}.")