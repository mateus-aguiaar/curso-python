weight = float(input("\nEnter your Weight: "))
height = float(input("\nEnter your height: "))
imc = weight / (height ** 2)

if imc < 18.5:
    print("\nUnderweight")

elif imc >= 18.5 and imc < 25:
    print("\nIdeal weight")

elif imc >= 25 and imc < 30:
    print("\nOverweight")

elif imc >=30 and imc <= 40:
    print("\nObesity")

else:
    print("\nMorbid obesity")

print(f"\nThis is your BMI value {imc:.2f}")