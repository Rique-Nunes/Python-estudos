import psycopg2

try:
    with psycopg2.connect(
        host='maximally-big-surfbird.data-1.use1.tembo.io',
        database='biblioteca', user='postgres',
        password='rU8AOWmFkV8VIIa5'
    )as con:
        consulta_sql = "select * from autor"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print("Foram retornados tantos dados: ", cursor.rowcount)

        print("\nMostrando os dados: ")
        for linha in linhas:
            print('idautor: ', linha[0])  # type: ignore
            print('nomeautor: ', linha[1])  # type: ignore
            print('sobrenomeautor: ', linha[2], "\n")  # type: ignore
except psycopg2.Error as erro:
    print("Erro ao realizar a operação: ", erro)

finally:
    cursor.close()
