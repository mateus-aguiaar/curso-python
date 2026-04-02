## nome = str(input('Digite o seu nome: '))

## if nome == 'Gustavo':
    ##print('Que nome lindo você tem!')

## else:
    ##print('Seu nome é tão normal')

## print(f'Bom dia, {nome}!')

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2
print(f'A sua média foi {media}')

if media >= 7:
    print('Aprovado')
    print('Parabéns pela média!')
else:
    print('Recuperação')
    