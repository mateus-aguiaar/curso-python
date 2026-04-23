ano = int(input('Enter the year to be analyzed or enter 0 to analyze the current year: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('The year is a leap year!')

else:
    print('It is not a leap year.')