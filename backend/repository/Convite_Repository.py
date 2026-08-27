class ConviteRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection


    def salvar(self, convite, db_connection=None):
        connection = db_connection or self.db_connection
        if connection:
            cursor = connection.cursor(dictionary=True)
            try:
                cursor = db_connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
                sql = "INSERT INTO convite_ativacao(token, criado_em, expira_em, utilizado, id_usuario) VALUES (%s, %s, %s, %s, %s)"
                valores = (convite.token, convite.criado_em, convite.expira_em, convite.utilizado, convite.id_usuario)

                cursor.execute(sql,valores)  # envia o comando  e os dados ao banco
        
                print(f"✅ Sucesso!.Convite salvo para o usuário {convite.id_usuario}.")

            finally:
                # Garante que o banco não fique sobrecarregado
                    cursor.close()
        else:
            print("O Repository parou porque a conexão com o banco de dados falhou.")

    def buscar_por_token(self, token, db_connection=None):

        connection = db_connection or self.db_connection
    
        if not connection:
            print("O Repository parou porque a conexão com o banco de dados falhou.")
        return None

        cursor = None 
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM convite_ativacao WHERE token = %s"
            cursor.execute(sql, (token,))
            
            resultado = cursor.fetchone() 
            return resultado
        except Exception as e:
            print(f"Erro ao buscar no banco: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
