text = str(input("\nEnter a text: ")).replace(" ", "").lower()
reverse = ""
for letra in text:
    reverse = letra + reverse

if reverse == text:
    print("\nIt's a palindrome.")
    
else:
    print("\nIt is not a palindrome.")