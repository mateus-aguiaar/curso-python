frase = str(input('Enter a sentence:')).strip().upper().replace(" ", '')

print(f'The letter A appears {frase.count('A')} times in the sentence.')

print(f'The letter A appeared at position {frase.find('A')+1}')

print(f'The letter A appeared for the last time at position {frase.rfind('A')+1}')