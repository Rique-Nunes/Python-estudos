ano = 2021
maiores = menores = 0

for c in range (0,7):
    c = int(input("Digite o ano de nascimento: "))
    if ano - c > 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} pessoas são maiores de idade e {menores} pessoas são menores de idade')