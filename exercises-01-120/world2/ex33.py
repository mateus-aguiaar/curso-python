valor_casa = float(input("Enter the house value: "))
salario_comprador = float(input("Enter your salary: "))
tempo_pagamento = int(input("How long will you be paying (in years)?  "))
tempo = tempo_pagamento * 12
valor_do_pagamento = valor_casa / tempo

if valor_do_pagamento > salario_comprador * 0.3:
    print("You will not be able to buy the house.")

else:
    print(f"You will buy the house in {tempo} installments of ${valor_do_pagamento:.2f}.")