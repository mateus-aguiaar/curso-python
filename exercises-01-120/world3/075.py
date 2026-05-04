values = []
pares = []
cont_9 = 0

for i in range(4):
    value = int(input("\nEnter a value: "))
    values.append(value)

numbers = tuple(values)
print("\nThe typed numbers were:", numbers)

for i in numbers:
    if i % 2 == 0:
        pares.append(i)
    if i == 9:
        cont_9 += 1
        
numbers_pares = tuple(pares)

if 3 in values:
    indices = numbers.index(3) + 1
    print(f"\nThe first position of number 3 is: {indices}")

else:
    print("\nNumber 3 was not typed.")

print(f"\nNine appeared {cont_9} times.")
print("\nThe even numbers typed were:", numbers_pares)