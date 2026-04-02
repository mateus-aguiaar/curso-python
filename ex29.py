salario = float(input('Digite o seu salário R$: '))

if salario >= 1250:
    aumento = salario * 1.10
    print(f'O salário com ajuste fica R${aumento:.2f}')

else:
    aumento_2 = salario * 1.15
    print(f'O salário com ajuste fica R${aumento_2:.2f}')