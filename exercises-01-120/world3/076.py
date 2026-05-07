list = ("Bread", 3.50, "Açaí", 26.90, "Red Bull", 9.90, "McDonald's", 54.90, "Ice Cream", 22.90)

print("PRICE LIST")
print("--" * 5)

for i in range(len(list)):
    if i % 2 == 0:
        print(f"{list[i]}................R$ {list[i+1]}")
print("--" * 14)