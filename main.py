import sqlite3
import json

# Conectando ao banco SQLite
conexao = sqlite3.connect('banco.db')

# Definindo objeto cursor para executar comando em SQL através do python
cursor = conexao.cursor()

# Inserindo valores genéricos na tabela
cursor.execute("INSERT INTO clientes VALUES ('Rafael', '400289922', 'rafael@gmail.com', '20765057760')")
conexao.commit()
cursor.execute("INSERT INTO clientes VALUES ('Carol', '200489922', 'carol@gmail.com', '20045057760')")
conexao.commit()
cursor.execute("INSERT INTO clientes VALUES ('Miguel', '200589922', 'rafael@gmail.com', '20055057760')")
conexao.commit()

# Selecionando a primeira tupla da tabela
cursor.execute("SELECT * FROM clientes LIMIT 1")
cliente = cursor.fetchone()

# Definindo os nomes das colunas
colunas = ['Nome', 'Telefone', 'Email', 'Cpf']

# Validando e criando um dicionário com os dados do cliente
if cliente is None:
    print("Nenhum cliente encontrado.")
else:
    cliente_dict = dict(zip(colunas, cliente))
    # Salvando os dados em um arquivo JSON
    with open('clientes.json', 'w') as arquivo_json:
        json.dump(cliente_dict, arquivo_json, indent=4)

print(cliente)

# Fechando a conexão com o banco de dados
cursor.close()
conexao.close()