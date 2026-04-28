number = int(input("\nEnter a value: "))
accumulator = 1
multiplication = number

while multiplication != 1:
    accumulator = accumulator * multiplication
    multiplication -= 1
    
print(f"\nThe factorial value is equal to {accumulator}")