list = []
for i in range(5):
    weight = float(input("\nEnter a weight: "))
    list.append(weight)

greatest = max(list)
minimum = min(list)

print(f"\nThe greatest weight was {greatest}kg")
print(f"\nThe lowest weight was {minimum}kg")