viagem = int(input('Quantos KM são a viagem? '))

if viagem <= 200:
    valor_ate_200 = 0.50 * viagem
    print(f'Você pagará R$ 0,50 por KM, totalizando {valor_ate_2002:.2f}')

else:
    valor_mais_200 = 0.45 * viagem
    print(f'Você pagará R$ 0,45 por KM, totalizando {valor_mais_200:.2f}')