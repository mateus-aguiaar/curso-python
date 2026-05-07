list = ("Bread", "Beans", "Mateus")

for word in list:
    vowel_accumulator = ""

    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowel_accumulator += letter

    print(f"\nThe word {word} contains the vowels {vowel_accumulator}")