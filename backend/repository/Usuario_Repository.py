from enum import Enum

class UsuarioRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def salvar(self, usuario, db_connection=None):
        connection = db_connection or self.db_connection
        if connection:
            try:
                cursor = connection.cursor(dictionary=True) # se usa dicionario para acessar o nome e nao posição dos dados
                sql = "INSERT INTO Usuario(nome, email, senha, perfil, id_empresa) VALUES (%s, %s, %s, %s, %s)"
                perfil_valor = getattr(usuario.perfil, 'value', usuario.perfil) # Se tiver 'value', pega o valor. Se não tiver, usa o próprio perfil como padrão.
                valores = (usuario.nome, usuario.email, usuario.senha, perfil_valor, usuario.id_empresa)

                cursor.execute(sql,valores)  # envia o comando  e os dados ao banco
            
                id_gerado = cursor.lastrowid
                print(f"✅ Sucesso! {usuario.email} salvo.")
                return id_gerado
            
            finally:
                # Garante que o banco não fique sobrecarregado
                cursor.close()
        else:
            print("O Repository parou porque a conexão com o banco de dados falhou.")


    def buscar_por_email(self, email, db_connection=None):
        connection = db_connection or self.db_connection
        if connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Usuario WHERE email = %s"
                cursor.execute(sql,(email,))
                resultado = cursor.fetchone() # traz o resultado do banco
                return resultado
            
            except Exception as e:
             
                print(f"Erro crítico ao buscar no banco: {e}")
                return None
            
            finally:
                cursor.close()
                    