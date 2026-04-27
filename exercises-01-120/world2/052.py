number = int(input("\nEnter a value: "))
cont = 0
for i in range(1,number + 1):
    if number % i == 0:
        cont += 1

print(f"\nThe number {number} was divisible {cont} times.")

if cont == 2:
    print("\nThe number is prime.")

else:
    print("\nThe number is not prime.")