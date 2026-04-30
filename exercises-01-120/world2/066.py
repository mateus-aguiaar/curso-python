number_count = 0
total = 0

while True:
    number = int(input("\nEnter a value, [999] to quit: "))
    if number != 999:
        number_count += 1
        total += number
    else:
        break

print(f"\nThe total sum of {number_count} numbers was {total}.")