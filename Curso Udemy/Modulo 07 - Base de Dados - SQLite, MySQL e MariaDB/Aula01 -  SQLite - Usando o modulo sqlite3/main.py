import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "nome TEXT NOT NULL,"
               "peso REAL"
               ")")

cursor.execute("INSERT INTO clientes(nome, peso) VALUES (?, ?)", ("Renan", 58.2))
conexao.commit()

cursor.execute("INSERT INTO clientes(nome, peso) VALUES (?, ?)", ("Ivan", 80.0))
conexao.commit()

cursor.execute("INSERT INTO clientes(nome, peso) VALUES (?, ?)", ("Maria", 56.5))
conexao.commit()


cursor.execute("UPDATE clientes SET nome=? WHERE id=?", ("Reinan", 1))


#cursor.execute("DELETE FROM clientes WHERE id=?", (1,))

#cursor.execute("SELECT * FROM clientes")

cursor.execute("SELECT nome,peso from clientes WHERE peso > ?", (70.0, ))

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()