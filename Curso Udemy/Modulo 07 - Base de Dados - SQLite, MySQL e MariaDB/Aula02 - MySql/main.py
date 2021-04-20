import pymysql.cursors


conexao = pymysql.connect(host='127.0.0.1',
                          port=3306,
                          user='root',
                          password='',
                          db='clientes',
                          charset='utf8mb4'
)

with conexao.cursor() as cursor:
    cursor.execute("INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s,%s,%s,%s)", ("Renan", "Bertolotti", 22, 58) )
    conexao.commit()

with conexao.cursor() as cursor:
    query = "INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s,%s,%s,%s)"
    dados = [
        ('Ivan', "Bertolotti", 23, 80.0),
        ("Edson", "Bertolotti", 58, 97.54),
    ]

    cursor.executemany(query, dados)
    conexao.commit()


with conexao.cursor() as cursor:
    cursor.execute("DELETE FROM clientes WHERE id=%s", (9,))
    conexao.commit()


with conexao.cursor() as cursor:
    query = "DELETE FROM clientes WHERE id IN (%s, %s, %s)"

    cursor.execute(query, (2, 4, 10))
    conexao.commit()


with conexao.cursor() as cursor:
    query = "UPDATE clientes SET nome=%s WHERE id=%s"

    cursor.execute(query, ("Ivan", 13))
    conexao.commit()


with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')

    for cod, nome, sobrenome, idade, peso in cursor.fetchall():
        print(cod, nome, sobrenome, idade, peso)


conexao.close()