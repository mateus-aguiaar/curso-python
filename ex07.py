# Calculador de litros para pintar uma parede.
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a alutra da parede: "))

area_parede = largura * altura
qtd_tinta = area_parede / 2

print("A quantidade necessaria para pintar uma parede de área {}m² é igual a {}L".format(area_parede,qtd_tinta))