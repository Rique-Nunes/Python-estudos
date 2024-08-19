# ordem dos operadores
# () depois ** (potenciação)
# * e / e // (divisão inteira) e % (porcentagem é resto)
# raiz por exemplo é 81**(1/2)
# limitar as casas decimais {:.3f}


# a = int(input("digite um valor"))
# print(f"o número é {a}, seu sucessor é {a+1} seu antecessor é {a-1}")

# b = int(input("digite a primeira nota do aluno"))
# c = int(input("digite a segunda nota"))
# print(f"a média desse aluno é {(b+c)/2}")

# d = int(input("escreva um valor me metros"))
# print(f"o valor {d}m em são {d*100}cm e {d*1000}mm")

# e = int(input("digite o número que quer ver sua taboada"))
# num = 0
# i = 0
# for i in range(0, 11):
#   resultado = e * i
#  print(f"\n|{e} x {i} = {resultado}|")

# altura = int(input("Tamanho da parede altura: "))
# largura = int(input("tamanho da parede largura"))
# area = altura*largura
# tinta = area/2
# print(f"para tal parede de {altura*largura}m² de área são necessários {tinta}")

aumento = float(input("quanto de porcentagem para aumentar? "))
diminui = float(input("quando de porcentagem para diminuir?"))
salario = float(input("salario é?"))

salarioplus = salario + (salario * (aumento/100))
salariominus = salario - (salario * (diminui/100))
print(f"o aumento seria {salarioplus} e a diminuição seria {salariominus}")
