price_produt = float(input("Enter the product price: "))
payment_option = int(input("\n[1] - Cash/check\n[2] - On sight card\n[3] - Card 2x \n[4] - Card 3x or more\nEnter your payment option: "))

if payment_option == 1:
    print(f"\nThe final price of the product with a 10% discount is ${price_produt - (price_produt * 0.10)}")

elif payment_option == 2:
    print(f"\nThe final price of the product with a 5% discount is ${price_produt - (price_produt * 0.05)}")

elif payment_option == 3:
    print(f"\nThe final price of the product when paid in 2 installments is ${price_produt / 2}")

elif payment_option == 4:
    installments = int(input("\nEnter the number of installments: "))
    print(f"\nThe final price of the product when paid in {installments} installments is ${(price_produt + (price_produt * 0.20)) / installments:.2f} with interest.")

else:
    print("\nInvalid payment method.")