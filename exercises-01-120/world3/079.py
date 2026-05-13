list = []
while True:
    values = int(input("\nEnter a value: "))
    if values not in list:
        list.append(values)
    else:
        print("\nValue already exists in the list.")
        break

print("list:", sorted(list))