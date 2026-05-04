serie_b = (
    "Fortaleza",
    "São Bernardo",
    "Sport Recife",
    "Operário",
    "Vila Nova",
    "Criciúma",
    "Juventude",
    "Náutico",
    "Ceará SC",
    "Botafogo SP",
    "Avaí",
    "Novorizontino",
    "Athletic",
    "Atlético-GO",
    "Cuiabá",
    "Ponte Preta",
    "Goiás",
    "CRB",
    "Londrina",
    "América-MG",
)
print("\nThe five first in the table are: ", (serie_b[0:5]))
print("\nThe four last placed are: ", (serie_b[-4:]))
serie_b_order = sorted(serie_b)
print(serie_b_order)
time = "Sport Recife"
posicao = serie_b.index(time) + 1
print(f"\nSport Clube Do Recife is in {posicao}rd place.")