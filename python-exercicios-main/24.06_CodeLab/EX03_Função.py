#Faça um programa com uma função chamada soma Imposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def imposto (taxaImposto, custo):
    imposto = (taxaImposto*custo)/100
    return imposto

taxaImposto = int(input("Digite o valor da taxa para aplicação [SEM %]: "))
custo = float(input("Digite o custo do valor: "))

imposto(taxaImposto, custo)
print(f'''Taxa de imposto: {taxaImposto}%
Custo do valor antes da aplicação da taxa: {custo}''')
print(f'Custo do valor após a aplicação da taxa: {imposto(taxaImposto, custo)}')