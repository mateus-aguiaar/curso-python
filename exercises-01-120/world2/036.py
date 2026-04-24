valor_casa = float(input("\nEnter the house value: "))
salario_comprador = float(input("\nEnter your salary: "))
tempo_pagamento = int(input("\nHow long will you be paying (in years)?  "))
tempo = tempo_pagamento * 12
valor_do_pagamento = valor_casa / tempo

if valor_do_pagamento > salario_comprador * 0.3:
    print("\nYou will not be able to buy the house.")

else:
    print(f"\nYou will buy the house in {tempo} installments of ${valor_do_pagamento:.2f}")