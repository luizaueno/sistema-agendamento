import mysql.connector # Aqui você chama o tradutor que o pip instalou
db_connection = None 
try:
    # Esta é a parte onde o Python estabele conexao com o seu MySQL
    db_connection = mysql.connector.connect(
        host="localhost",      # O banco está no seu próprio PC
        user="root",           # Usuário padrão do MySQL
        password="admin123",  # A senha do banco
        database="mydb"        # O nome do banco 
    )

    # Verificação lógica: a porta abriu?
    if db_connection.is_connected():
        print("✅ Conexão estabelecida com sucesso!")
        
        cursor = db_connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
        sql = "INSERT INTO Empresa(nome, cnpj) VALUES (%s, %s)"
        valores = ("EmpresaTeste", "23-145.643/0001-98")
        cursor.execute(sql,valores)
        db_connection.commit()

except Exception as e:
    # Se der erro (senha errada, banco desligado), ele cai aqui
    print(f"Ops! Não consegui conectar. O erro foi: {e}")

finally:
    if db_connection and db_connection.is_connected():
        db_connection.close()
        print("Conexão fechada com segurança.")
