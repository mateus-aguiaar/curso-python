total_value = 0
product_over_1000 = 0
cheapest_product = 0
first_product = 0
cheapest_product_name = ''
while True:
    product_name = input("\nEnter the product name: ")
    product_value = float(input("\nEnter the product price, $"))
    first_product += 1
    total_value += product_value
    print("\n[1] - continue\n[2] - quit")
    option = int(input("Enter the desired option: "))
    if first_product == 1 or product_value < cheapest_product:
        cheapest_product = product_value
        cheapest_product_name = product_name
    if product_value > 1000:
        product_over_1000 += 1

    if option == 2:
        break
print("\nEnd of program")
print(f"\nThe total amount spent on shopping is ${total_value}")
print(f"\nThe number of products over $1000 was {product_over_1000} product(s).")
print(f"\nThe cheapest product was {cheapest_product_name} which costs ${cheapest_product}")