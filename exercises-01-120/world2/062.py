first_term = int(input("\nEnter a first term: "))
ratio = int(input("\nEnter a ratio for a.p: "))
term = first_term
cont = 1
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print(f"{term}", end = " → ")
        term += ratio
        cont += 1
    print("Pause")
    more = int(input("\nHow many terms do you want to show more? "))
print("\nEnd")
print(f"Progression ended with {total} terms shown.")