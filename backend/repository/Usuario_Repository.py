from infra.conexao_db import criar_conexao

class UsuarioRepository:
    def salvar(self, usuario):
        db_connection = criar_conexao() # tenta ganhar a conexao aberta da pasta infra
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
                sql = "INSERT INTO Usuario(nome, email, senha, perfil) VALUES (%s, %s, %s, %s)"
                valores = (usuario.nome, usuario.email, usuario.senha, usuario.perfil)

                cursor.execute(sql,valores)  # envia o comando  e os dados ao banco
                db_connection.commit() # confirma e salva permanentemente
                print(f"✅ Sucesso! {usuario.email} salvo.")

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


    def buscar_por_email(self, email):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Usuario WHERE email = %s"
                cursor.execute(sql,(email,))
                resultado = cursor.fetchone() # traz o resultado do banco
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()