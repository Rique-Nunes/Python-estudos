#01- Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa
ura = " "
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
operacao = 0

while ura not in "5":   
    ura = str(input('''Digite a opção que deseja
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Opção: '''))
    
    if ura == "1":
        operacao = n1 + n2
        print(f'A soma é: {operacao}\n')
    elif ura == "2":
        operacao = n1*n2
        print(f'A multiplicação é: {operacao}\n')
    elif ura == "3":
        if n1 > n2:
            print(f'O maior número é: {n1}\n')
        else:
            print(f'O maior numero é: {n2}\n')
    elif ura == "4":
        n1 = int(input("Digite o novo número: "))
        n2 = int(input("Digite o novo número: "))

    elif ura == "5":
        print("Saindo do programa...")
    else:
        print("Opção invalida tente novamente")
