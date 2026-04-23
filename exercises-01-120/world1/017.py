from math import hypot

cateto_oposto = float(input("Enter the value of the opposite side: "))
cateto_adjacente = float(input("Enter the value of the adjacent side: "))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(f"A right triangle with an opposite side equal to {cateto_oposto} and an adjacent side equal to {cateto_adjacente}, has its hypotenuse equal to {(hipotenusa):.2f} ")