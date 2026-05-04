import random 

random_numbers = []

for i in range(5):
    number = random.randint(1,100)
    random_numbers.append(number)

print(random_numbers)
print("\nO menor valor da lista é:",min(random_numbers))
print("\nO maior valor da lista é:",max(random_numbers))