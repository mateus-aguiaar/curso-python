sum = 0
cont = 0
for i in range(1,500 + 1):
    if i % 2 != 0 and i % 3 == 0:
        sum += i
        cont += 1

print(f"\nThe sum of the odd numbers that are multiples of 3 is {sum}.")
print(f"\nThe total number of values added was: {cont}.")