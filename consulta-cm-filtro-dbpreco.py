import sqlite3

nome = input("Nome do produto: ")

conexao = sqlite3.connect('preços.db')

cursor = conexao.cursor()


cursor.execute('select * from preços where nomeP = "%s"'% nome)
#cursor.execute('select * from preços where nomeP = ?', (nome,))

#x = 0
while True:
    result = cursor.fetchone()

    if result == None:
#        if x == 0:
#            print("Nada encontrado!")
        break
    print("Nome: %s\nPreço: %s" % result)
#    x += 1
    
cursor.close()
conexao.close()
