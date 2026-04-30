while True:
    withdrawn = int(input("Enter a value: "))
    notas_50 = withdrawn // 50 
    notas_20 = (withdrawn % 50) // 20
    notas_10 = ((withdrawn % 50) % 20) // 10
    nota_1 = ((withdrawn % 50) % 20) % 10

    print(f"\nThe quantity of 50$ notes was: {notas_50}")
    print(f"\nThe quantity of 50$ notes was: {notas_20}")
    print(f"\nThe quantity of 50$ notes was: {notas_10}")
    print(f"\nThe quantity of 50$ notes was: {nota_1}")