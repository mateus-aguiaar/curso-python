viagem = int(input('How many KM is the trip? '))

if viagem <= 200:
    valor_ate_200 = 0.50 * viagem
    print(f'You will pay $0.50 per KM, totaling {valor_ate_200:.2f}')

else:
    valor_mais_200 = 0.45 * viagem
    print(f'You will pay $0.45 per KM, totaling {valor_mais_200:.2f}')