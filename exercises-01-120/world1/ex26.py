velocidade = int(input('Car speed: '))
valor_multa = 0

if velocidade > 80:
    valor_multa = 7 * (velocidade - 80)
    print(f'You were fined and must pay {valor_multa} !')
else:
    print('You were under 80km/h, no fine required.')