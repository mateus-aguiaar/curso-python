term = int(input("\nHow many terms do you want to display?  "))
t1 = 0
t2 = 1
cont = 3
print(f" {t1} → {t2} → ", end= "")
while cont <= term:
    t3 = t1 + t2
    print(f" {t3} → ", end="")
    t1 = t2
    t2 = t3
    cont += 1
print("End")