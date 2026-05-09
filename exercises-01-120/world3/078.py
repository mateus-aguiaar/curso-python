list = []
for i in range(5):
    numbers = int(input("Enter a value: "))
    list.append(numbers)

max_number = (max(list))
lenght_max = list.index(max_number)
min_number = (min(list))
lenght_min = list.index(min_number)

print(f"\nThe largest value in the list is {max_number}, in position {lenght_max}")
print(f"\nThe smallest value in the list is {min_number}, in position {lenght_min}")