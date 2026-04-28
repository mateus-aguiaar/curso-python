gender = str(input("\nEnter your gender,[M] or [F]: ")).upper().strip()
while gender not in "MF" :
    gender = str(input("\nInvalid data, please re-enter your gender, [M] or [F]: ")).upper().strip()

print(f"\nGenre {gender} successfully registered.")