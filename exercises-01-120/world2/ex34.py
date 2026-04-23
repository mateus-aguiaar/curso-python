numero = int(input("\nEnter any integer value: "))
base = int(input("\n1- Binary\n2- Octal\n3- Hexadecimal\nEnter which base you want to convert to: "))

numero_binario = bin(numero)[2:]
numero_octal = oct(numero)
numero_hexa = hex(numero)

if base == 1:
    print(f"\nThe number {numero} in binary is {numero_binario}.")

elif base == 2:
    print(f"\nThe number {numero} in octal is {numero_octal}.")

else:
    print(f"\nThe number {numero} in hexadecimal is {numero_hexa}.")