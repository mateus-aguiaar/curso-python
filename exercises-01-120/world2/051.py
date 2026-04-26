first_term = int(input("\nEnter a first term: "))
ratio = int(input("\nEnter a ratio for p.a: "))
tenth = first_term + (10-1) * ratio

print("\nThe first ten terms of the arithmetic progression:")
for i in range(first_term, tenth + ratio , ratio):
    print(f"{i}", end = " → ")