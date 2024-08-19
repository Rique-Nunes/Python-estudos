#Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def IMC(peso, altura):
    IMC = peso/(altura*altura)
    if IMC < 18.5:
        return f'MAGREZA'
    elif 18.5 <= IMC >= 24.9:
        return f'NORMAL'
    elif 25.0 <= IMC >= 29.9:
        return f'SOBREPESO'
    elif 30 <= IMC >= 39.9:
        return f'OBESIDADE'
    else:
        return f'OBESIDADE GRAVE'
    
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print(f'''Sua altura {altura}
Seu peso {peso}Kg
Seu IMC é {IMC(peso,altura)}''')