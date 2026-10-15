
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
                cursor = connection.cursor(dictionary=True)
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
                
                # 🖥️ QUERY COM LIMPEZA DE STRING LITERAL 'None' DIRETO NO BANCO:
                # Se o campo telefone for 'None', o MySQL retorna '' (vazio)
                sql = """
                    SELECT 
                        P.idprofissional AS id, 
                        COALESCE(U.nome, P.nome, 'Sem Nome') AS nome, 
                        COALESCE(P.especialidade, '') AS especialidade, 
                        IF(P.CNPJ = 'None', '', COALESCE(P.CNPJ, '')) AS cnpj, 
                        IF(P.telefone = 'None', '', COALESCE(P.telefone, '')) AS telefone, 
                        COALESCE(P.cor, '#E3E7ED') AS cor,
                        CASE 
                            WHEN C.utilizado = 1 THEN 'Conta ativa'
                            ELSE 'Convite pendente'
                        END AS status,
                        IF(U.email = 'None', '', COALESCE(U.email, '')) AS email
                    FROM profissional P 
                    LEFT JOIN usuario U ON P.id_usuario = U.id_usuario
                    LEFT JOIN convite_ativacao C ON P.id_usuario = C.id_usuario
                """
                
                cursor.execute(sql)
                resultado = cursor.fetchall() 
                return resultado
            except Exception as e:
                print(f"❌ ERRO AO BUSCAR DADOS COMPLETOS: {e}")
                return None
            finally:
                cursor.close()
