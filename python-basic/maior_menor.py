# for, um loop de repetição para criar um fatorial de um número menor ao maior
# basicamente pega o menor = num, printa ele, adiciona o valor atual em um contador
# adiciona +1 para avançar o loop até a igualdade de num==m ser verdadeira
# e depois printa o contador que foi somando ao longo do loop
num = int(input("digite o número menor \n"))
m = int(input("digite o número maior \n"))
contador = 0
n = 0

for num in range(num, m):
    print("\n", num)
    contador += num
    num += 1
print("\n", num)

contador += num

print(" a soma dessa ordem é: ", contador)
