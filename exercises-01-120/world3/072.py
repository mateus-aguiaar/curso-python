numbers = (
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    "twenty"
)
while True:
    chosen_number = int(input("\nEnter a value,from 0 to 20: "))
    if chosen_number > 20:
        print("\nType it again")
    else:
        break

print("\nNumber:",numbers[chosen_number])