from backend.infra.conexao_db import criar_conexao # funcao da pasta infra
db_connection = criar_conexao() # tenta ganhar a conexao aberta da pasta infra
if db_connection:
    try:
        cursor = db_connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
        sql = "INSERT INTO Empresa(nome, cnpj) VALUES (%s, %s)"
        valores = ("EmpresaNovoteste", "34-897.732/0001-04")

        cursor.execute(sql,valores)
        db_connection.commit()
        print(f"✅ Sucesso! {valores[0]} salva no banco.")

    except Exception as e:
        print(f"Erro no Repository: {e}")

    finally:
        # Garante que o banco não fique sobrecarregado
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("✅ Conexão encerrada com segurança.")
else:
    print("O Repository parou porque a Infra falhou.")