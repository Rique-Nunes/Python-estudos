#01-Faça um programa que leia o peso de cinco pessoas.No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 9999

for c in range(0 ,5):
    c = float(input("Digite seu peso: "))
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'Maior peso {maior} e Menor peso {menor}')
