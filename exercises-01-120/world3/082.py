list = []
list_par = []
list_impar = []

while True:
    values = int(input("\nEnter a value: "))
    list.append(values)
    option = input("Do you want to continue? [Y/N] ").upper()
    if option == "Y":

        print("\nEnter a new value.")
    else:
        break
for numbers in list:
    if numbers % 2 == 0:
        list_par.append(numbers)
    else:
        list_impar.append(numbers)

print(f"\nThe list of entered values is: {list}")
print(f"\nThe list of even values is: {list_par}")
print(f"\nThe list of odd values is: {list_impar}")