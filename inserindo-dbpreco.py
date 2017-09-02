import sqlite3

# Inserindo produtos e preços.
dados = [("Feijão", "4.99"),
         ("Farinha","7.00"),
         ("Nissin","0.65")]

conexao = sqlite3.connect('preços.db')

cur = conexao.cursor()
cur.executemany('''
    insert into preços(nomeP, precoP)
    values(?, ?)
    ''', dados)

conexao.commit()
cur.close()
conexao.close()
