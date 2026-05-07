import random

random_numbers = []

for i in range(5):
    number = random.randint(1,100)
    random_numbers.append(number)

print("The numbers drawn were:",random_numbers)
print("\nThe smallest value in the list is:",min(random_numbers))
print("\nThe largest value in the list is:",max(random_numbers))