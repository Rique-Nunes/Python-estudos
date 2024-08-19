lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
linha = 1
coluna = 1
print("Digite o valores necessários para o complemetno da matriz")

for num in range(0, 3, 1):
    for number in range(0, 4, 1):
        lista[num][number] = int(
            input("\n escreva um número para a posição {} \n ".format(lista[num][number])))

for number in range(0, 3, 1):
    for num in range(0, 4, 1):
        if lista[number][num] <= 0:
            lista[number][num] = 0

        print("\n os números digitados na ordem e em suas respectivas posições são: {}".format(
            lista[number][num]))
