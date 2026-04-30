i = 0
while True:
    table = int(input("\nEnter the multiplication table you want: "))
    print("------" * 5)
    if table < 0:
        print("\nEnd of program, see you next time!")
        break

    for i in range(1, 10 + 1):
        print(f"{table} x {i} = {table * i}")