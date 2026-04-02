velocidade = int(input('Velocidade do carro: '))
valor_multa = 0
if velocidade > 80:
    valor_multa = 7 * (velocidade - 80)
    print(f'Você foi multado e deverá pagar {valor_multa} !')
else:
    print('Você estava a baixo de 80km/h, não deverá pagar multa.')
    
