km = float(input("Informe a quantidade de km pecorrido com o carro: "))
dias = int(input("Informe quantos dias você utilizou o carro: "))

valor_total = (dias * 60) + (km * 0.15)

print(f"O cliente passou {dias} dias com o carro, pecorreu {km}km, o valor total será R${valor_total}")