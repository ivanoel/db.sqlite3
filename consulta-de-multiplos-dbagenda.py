import sqlite3

conexao = sqlite3.connect("preços.db")

cursor = conexao.cursor()

cursor.execute("select * from preços")



# O método fetchall() retorna uma lista com resultados de nossa consulta.
result = cursor.fetchall()


# A variavel registro para exibir os dados.
for registro in result:
    print("Nome: %s\nPreço: %s"%(registro))



"""
Consulta, regitro por registro.



while True:

# O método fetchone() sendo usando dentro while.
# Como nao sabemos quantos registros serão retornados utilizamos
# while True, que eh interrompido quando o método fetchone retorna (None).
    result = cursor.fetchone()
    if result == None:
        break
    print("Nome: %s\nPreço:%s"%(result))
"""

cursor.close()
conexao.close()
