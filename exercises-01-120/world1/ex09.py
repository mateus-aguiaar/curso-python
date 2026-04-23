largura = float(input("Enter the width of the wall: "))
altura = float(input("Enter the height of the wall: "))

area_parede = largura * altura
qtd_tinta = area_parede / 2

print("The amount needed to paint a wall with an area of {}m² is equal to {}L".format(area_parede,qtd_tinta))