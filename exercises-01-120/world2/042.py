comprimento1 = float(input('\nEnter the length of a line: '))
comprimento2 = float(input('\nEnter the length of a line: '))
comprimento3 = float(input('\nEnter the length of a line: '))

if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print('\nIt is possible to form a triangle')
    if comprimento1 == comprimento2 == comprimento3:
        print("\nequilateral triangle ")

    elif comprimento1 == comprimento2 != comprimento3 or comprimento2 == comprimento3 != comprimento1 or comprimento1 == comprimento3 != comprimento2:
        print("\nIsosceles triangle")
     
    else:
        print("\nScalene triangle")
else:
    print('\nIt is not possible to form a triangle')