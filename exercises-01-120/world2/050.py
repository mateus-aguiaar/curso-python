cont = 0
sum = 0
for i in range(0,6):
    number = int(input("\nEnter a value: "))
    if number % 2 == 0:
        sum += number
        cont +=1

print(f"\nThe sum of {cont} even numbers given is equal to {sum}.")