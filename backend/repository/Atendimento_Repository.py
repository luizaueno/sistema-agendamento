from infra.conexao_db import criar_conexao

class AtendimentoRepository:
    def salvar(self, atendimento):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True) # faz a conexao entre python e db, executando os comandos de fato, se usa dicionário para acessar o nome do dado não posição
                sql = "INSERT INTO Atendimento( id_paciente, id_profissional, status, data, hora_inicio, hora_fim) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (atendimento.id_paciente, atendimento.id_profissional, atendimento.status, atendimento.data, atendimento.hora_inicio, atendimento.hora_fim)

                cursor.execute(sql, valores)
                db_connection.commit()
                print(f"✅ Sucesso! {atendimento} salvo")
            
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

    def buscar_por_status(self, status):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Atendimento WHERE status = %s"
                cursor.execute(sql,(status,))
                resultado = cursor.fetchall()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()

    def buscar_por_paciente(self, id_paciente):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Atendimento WHERE id_paciente = %s"
                cursor.execute(sql,(id_paciente))
                resultado = cursor.fetchall()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()

    def buscar_por_profissional(self, profissional):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Atendimento WHERE profissional = %s"
                cursor.execute(sql,(profissional,))
                resultado = cursor.fetchone()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()

    def buscar_por_data(self, data):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Atendimento WHERE data = %s"
                cursor.execute(sql,(data,))
                resultado = cursor.fetchone()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()

    def verificar_disponibilidade(self, id_profissional, data, hora_inicio, hora_fim):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Atendimento WHERE id_profissional = %s and data = %s and hora_inicio = %s and hora_fim = %s"
                cursor.execute(sql,(id_profissional, data, hora_inicio, hora_fim))
                resultado = cursor.fetchall()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()
    