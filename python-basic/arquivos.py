# Manipulação de arquivos de texto


# Metodo read
# print(f'método read(): \n')
# print(manipulador.read())

# metodo readline
# print(manipulador.readline())

# metodo readlines
# print(manipulador.readlines())

# a parte do arquivo.txt pode ser substituida pelo caminho de um arquivo
# que está em outra pasta ao usar o caminho relativo C:\\ com barras duplas
# texto = input('digite a palavra')
# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'a string foi encontrada')
#             print(linha)
#         else:
#             print(f'Nesta linha não foi encontrada')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

# Escrever em um arquivo de texto
# texto = '\nPython é bão demais'
# try:
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write(texto)
#     manipulador.write('\nInteligencia artificial veio para ficar')
# except IOError:
#     print(f'não foi possivel abrir o arquivo')
# else:
#     manipulador.close()

# criar e gravar o arquivo com listas
frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora']
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'não foi possivel abrir o arquivo')
else:
    manipulador.close()

# ler o arquivo criado
try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()
