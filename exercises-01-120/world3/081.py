list = []
cont_values = 0

while True:
    values = int(input("\nEnter a value: "))
    list.append(values)
    cont_values += 1
    option = input("Do you want to continue? [Y/N] ").upper()
    if option == "N":
        break
    else:
        print("\nEnter a new value.")

print(f"\n{cont_values} values were entered.")
print(f"\nThe list of entered values in descending order is: {sorted(list, reverse=True)}")

if 5 in list:
    print("\nThe value 5 was found in the list.")
else:
    print("\nThe value 5 was not found in the list.")