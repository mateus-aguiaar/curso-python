frase = str(input('Digite uma frase:')).strip().upper().replace(" ", '')


print(f'A letra A aparece {frase.count('A')} vezes na frase.')

print(f'A letra A apareceu na posição {frase.find('A')+1}')

print(f'A letra A apareceu pela ultima vez na posição {frase.rfind('A')+1}')