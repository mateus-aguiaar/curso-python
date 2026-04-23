salario = float(input('Enter your salary $: '))

if salario >= 1250:
    aumento = salario * 1.10
    print(f'The adjusted salary is ${aumento:.2f}')

else:
    aumento_2 = salario * 1.15
    print(f'The adjusted salary is ${aumento_2:.2f}')