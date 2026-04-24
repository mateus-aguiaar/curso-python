score1 = float(input("\nEnter your first note: "))
score2 = float(input("\nEnter your second note: "))

average = (score1 + score2) / 2

if average >= 7:
    print("\nThe student was approved")

elif average >= 5:
    print("\nThe student failed the course.")

else:
    print("\nThe student failed.")