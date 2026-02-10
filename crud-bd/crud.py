import sqlite3

conexao = sqlite3.connect('utilizadores.db')

cursor = conexao.cursor()

cursor.execute('''

    create table if not exists utilizadores (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  email VARCHAR(30) UNIQUE
               
                  )
''')

cursor.execute('''  
    insert into utilizadores (nome,email) values (?,?)''',

                 ('Amias Senda', 'amias.senda@faci-x.ao'),
    
                 )

conexao.commit()


cursor.execute('select * from utilizadores')
result = cursor.fetchall()

for u in result:
    print(u)






conexao.close()
