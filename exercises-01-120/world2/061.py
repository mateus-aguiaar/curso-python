first_term = int(input("\nEnter a first term: "))
ratio = int(input("\nEnter a ratio for p.a: "))
term = first_term
cont = 1

while cont <= 10:
    print(f"{term}", end = " → ")
    term += ratio
    cont += 1
    
print("End")