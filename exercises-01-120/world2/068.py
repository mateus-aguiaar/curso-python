import random

consecutive_wins = 0
while True:
    play_computer = random.randint(0, 10)
    play_player = int(input("\nEnter a value: "))
    total = play_computer + play_player
    option = input("Even or odd, [E] or [O]: ").upper()
    print(total)
    print(play_computer)

    if option == "E" and total % 2 == 0 or option == "O" and total % 2 != 0:
        consecutive_wins += 1
        print("\n\033[1;32mPlayer wins.\033[m")

    elif option == "E" and total % 2 != 0 or option == "O" and total % 2 == 0:
        print("\n\033[1;31mComputer wins.\033[m")
        break

    else:
        print("\nInvalid option, please try again:")

print(f"\nThe number of consecutive wins was {consecutive_wins}.")