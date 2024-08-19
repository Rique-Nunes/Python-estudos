import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        global con
        con = mysql.connector.connect(
            host='localhost', database='biblioteca', user='root', password='12012006')
    except Error as erro:
        print("Erro de conexão", erro)


def visualizar(idproduto):
    try:
        conectar()
        cursor = con.cursor()
        comando = f"SELECT * FROM teste_produtos where idproduto = %s"
        cursor.execute(comando, (idproduto,))
        linha = cursor.fetchall()
        if len(linha) > 0:
            for linhas in linha:
                print('idproduto: ', linhas[0])  # type: ignore
                print('nome: ', linhas[1])  # type: ignore
                print('preço: ', linhas[2])  # type: ignore
                print('quantidade: ', linhas[3])  # type: ignore
        else:
            print(f"Produto com id {idproduto} não encontrado!!")
            exit()
    except Error as erro:
        print("Erro na visualização do dado!", erro)
    finally:
        cursor.close()
        con.close()


def deletar(idproduto):
    try:
        conectar()
        cursor = con.cursor()
        comando = f"DELETE FROM teste_produtos where idproduto = %s"
        cursor.execute(comando, (idproduto,))
        con.commit()
        print("Produto deletado com sucesso!")
        exit()
    except Error as erro:
        print("Erro na visualização do dado!", erro)
    finally:
        cursor.close()
        con.close()


def atualizar(id_produto):
    try:
        conectar()
        preco = input("Digite o novo valor: ")
        comando = f"UPDATE teste_produtos set preco = {preco} where idproduto = {id_produto}"
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        print("Atualização realizada com sucesso!")
    except Error as erro:
        print("Erro na atualização", erro)
    finally:
        cursor.close()
        con.close()

# Validar a entrada do usuário


if __name__ == "__main__":
    print("Iniciaização teste operacional do banco de dados")
    print("Siga os passos")

    # visualizar
    produto_id = input("Digite o id do produto: ")
    visualizar(produto_id)

    # deletar
    response = input("Deseja deletar o produto? (s/n)")
    if response.lower() == 's':
        deletar(produto_id)

    # Atualizar
    response = input("Deseja atualizar o preço? (s/n)")
    if response.lower() == 's':
        atualizar(produto_id)
        verificar = input("deseja visualizar a mudança? (s/n)")
        if verificar.lower() == 's':
            visualizar(produto_id)
            print("Obrigado por utilizar de nossos serviços")
        else:
            print("Obrigado por utilizar de nossos serviços")
    else:
        print("Tenha um bom dia!")
