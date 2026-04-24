import random
options = ['rock', 'paper', 'scissors']
player_move = str(input("\nEnter your move: "))
computer_move = random.choice(options)

if player_move == "rock" and computer_move == "scissors":
    print("\nPlayer win!")

elif player_move == "scissors" and computer_move == "rock":
    print("\nComputer win!")

elif player_move == "scissors" and computer_move == "paper":
    print("\nPlayer win!")

elif player_move == "paper" and computer_move == "scissors":
     print("\nComputer win!")

elif player_move == "paper" and computer_move == "rock":
    print("\nPlayer win!")

elif player_move == "rock" and computer_move == "paper":
    print("\nComputer win!")

else:
    print("\nDraw.")

print(f"\nThe choice of computer was {computer_move}.")