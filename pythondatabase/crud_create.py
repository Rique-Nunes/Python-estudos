import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost', database='biblioteca', user='root', password='12012006')

    criar_tabela_sql = """CREATE TABLE teste_produtos(
                            idproduto INT(11) NOT NULL,
                            nomeproduto VARCHAR(70),
                            preco FLOAT NOT NULL,
                            quantidade TINYINT NOT NULL,
                            PRIMARY KEY (idproduto)); """
    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print("tabela criada com sucesso")
except mysql.connector.Error as erro:
    print("falha ao criar tabela no Mysql: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao Mysql finalizada")
print("Fim")
