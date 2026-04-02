
ano = int(input('Digite o ano a ser analisado ou digite 0 para analisar o ano atual: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')

else:
    print('Não é bissexto.')