#Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

horas = int(input("Horas trabalhadas no mês: "))
salario = int(input("Digite seu salario mensal: "))

salarioExtra = 0
horasTrab = salario/horas

extra = horas

if horas > 40:
    extra = extra - 40
    for e in range (extra):
        salarioExtra = horasTrab * 1.5
        salarioExtra = salario * 8
    print(f'Salario com hora extra: {salarioExtra}')
else:
    salario = salario*horas
    print(f'Salario sem hora extra: {salario}')