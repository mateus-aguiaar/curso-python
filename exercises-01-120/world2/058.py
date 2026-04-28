import random
hit = False
guesses = 0
draw = random.randint(0,10)

while not hit:
    choice = int(input('\nEnter your number choice from 1 to 10: '))
    guesses += 1
    if choice == draw:
        print("\nYou got it right!")
        hit = True
    else:
        if choice < draw:
            print("\nMore...Try again ")
        else:
            print("\nLess...Try again")

print(f"\nTo get the correct answer, you made {guesses} guesses.")