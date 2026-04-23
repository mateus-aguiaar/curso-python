km = float(input("Enter the amount of km driven with the car: "))
dias = int(input("Enter how many days you used the car: "))

valor_total = (dias * 60) + (km * 0.15)

print(f"The customer spent {dias} days with the car, drove {km}km, the total value will be ${valor_total}")