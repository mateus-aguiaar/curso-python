comprimento1 = float(input('Enter the length of a line: '))
comprimento2 = float(input('Enter the length of a line: '))
comprimento3 = float(input('Enter the length of a line: '))

if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print('It is possible to form a triangle')

else:
    print('It is not possible to form a triangle')