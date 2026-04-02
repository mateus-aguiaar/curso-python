comprimento1 = float(input('Digite o comprimento de uma reta: '))
comprimento2 = float(input('Digite o comprimento de uma reta: '))
comprimento3 = float(input('Digite o comprimento de uma reta: '))

if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print('É póssivel formar um triângulo')

else:
    print('Não é póssivel formar um triângulo')