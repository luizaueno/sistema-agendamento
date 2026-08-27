
class ProfissionalRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def salvar(self, profissional, db_connection=None):
        connection = db_connection or self.db_connection
        if connection:
            try:
                cursor = connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
                sql = "INSERT INTO Profissional(nome, CNPJ, especialidade, telefone, cor, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (profissional.nome, profissional.cnpj, profissional.especialidade, profissional.telefone, profissional.cor, profissional.id_usuario)
                print(f"✅ Sucesso! Profissional {profissional.nome} salvo no banco.")
                cursor.execute(sql,valores)  # envia o comando  e os dados ao banco
            finally:
                # Garante que o banco não fique sobrecarregado
                    cursor.close()
        else:
            print("O Repository parou porque a conexão com o banco de dados falhou.")


    def buscar_por_cnpj(self, cnpj, db_connection=None):
        connection = db_connection or self.db_connection
        if connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Profissional WHERE cnpj = %s"
                cursor.execute(sql,(cnpj,))
                resultado = cursor.fetchone() # traz o resultado do banco
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
            
                cursor.close()
            
    
    def buscar_todos(self, db_connection = None):
        connection = db_connection or self.db_connection
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                sql = "SELECT P.id, P.nome, P.especialidade, C.status_convite FROM Profissional P LEFT JOIN convite_ativacao C ON P.id_usuario = C.id_usuario"
                cursor.execute(sql)
                resultado = cursor.fetchall() 
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                cursor.close()
                    