import sqlite3


#conectei meu banco de dados 
connection = sqlite3.connect('novo_db.db')
#cursor que vai executar o comando sqlite(conectar o banco)
cursor = connection.cursor()

#criando minha tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTERGER)'''
)

#inserir dados na tabela

cursor.execute(
    "INSERT INTO usuarios (nome, idade) VALUES ('João', 25)"
)

#fazer uma consulta de dados

cursor.execute(
    'SELECT * FROM usuarios'
)
rows = cursor.fetchall()
for row in rows:
    print(row) 
    # printa o resultado que inseri no banco de dados 

#fecha minha conexão do banco de dados
connection.commit()
#fecha minha conexão 
connection.close()