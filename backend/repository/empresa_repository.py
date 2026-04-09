from infra.conexao_db import criar_conexao

class EmpresaRepository:
    def salvar(self, empresa):
        db_connection = criar_conexao() # tenta ganhar a conexao aberta da pasta infra
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
                sql = "INSERT INTO Empresa(nome, cnpj) VALUES (%s, %s)"
                valores = (empresa.nome, empresa.cnpj)

                cursor.execute(sql,valores)
                db_connection.commit()
                print(f"✅ Sucesso! {empresa.nome} salva.")

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


    def buscar_por_cnpj(self, cnpj):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Empresa WHERE cnpj = %s"
                cursor.execute(sql,(cnpj,))
                resultado = cursor.fetchone() # traz o resultado do banco
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()