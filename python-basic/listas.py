# listas representam uma sequencia de valores

# sintaxe: nome_lista = [valores]
# notas = [5, 7, 8, 9, 7]
# print(notas)


n1 = ["a", "b", "c", "d"]
n2 = [1, 23, 4, 5, 67, 32, 1]
# print(", ".join(n1))
# valores = n1+n2 somar as listas
# valores[0] = 9 modificar um item da lista
# print(len(valores))   ler quantos elementos a lista tem
# print(sorted(valores))    ler a lista ordenada
# print(sorted(valores, reverse=True)) invertida
# print(sum(valores)) soma
# print(min(valores)) valor minimo
# print(max(valores)) valor maximo
# n1.append(13) adiciona um item ao final da lista
# print(n1)
# n1.pop(2)  remove um item especifico (se nao especificar será o ultimo)
# print(n1)
# n1.remove("a") remove um item que voce disser que tem
# n1.insert(1, 31)  insere um item e empurra os outros mais pra frente na lsita
# print(n1)
# print(7 in n1) verifica se 7 pertence a lista (retornar true ou false boolean)

bebidas = []
while True:
    print("Olá - Seja Bem-Vindo")
    pedido = 0
    pedido = str(input(
        "Gostaria de digitar sua bebida? \n 1-Adicionar bebida \n 2-Remover bebida \n 3-Parar e mostrar"))
    if pedido == "1":
        bebidas.append(str(input("Digite a sua bebida: ")))
        bebidas.sort()
    elif pedido == "2":
        for drinks in bebidas:
            print(drinks)
        # print(', '.join(bebidas))
        remove = str(input("\nqual bebida deseja remover?"))
        bebidas.remove(remove)
    elif pedido == "3":
        for drinks in bebidas:
            print(drinks)
        # print(', '.join(bebidas))
        print("\n Obrigado pela preferencia!! ")
        break
    else:
        print("Erro, digite novamente!")
