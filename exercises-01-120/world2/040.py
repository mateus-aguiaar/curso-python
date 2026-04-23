score1 = float(input("\nEnter your first note: "))
score2 = float(input("\nEnter your second note: "))

average = (score1 + score2) / 2

if average >= 7:
    print("\nApproved")

elif average >= 5:
    print("\nRecovery")

else:
    print("\nFailed")