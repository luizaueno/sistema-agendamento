from infra.conexao_db import criar_conexao

class ProntuarioRepository:

    def prontuarioexistente(self, id_paciente):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Prontuario WHERE id_paciente = %s"
                cursor.execute(sql,(id_paciente,))
                resultado = cursor.fetchone()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()


    def salvar(self, prontuario):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "INSERT INTO Prontuario(id_paciente, diagnostico, plano_terapeutico) VALUES (%s, %s, %s)"
                valores = (prontuario.id_paciente, prontuario.diagnostico, prontuario.plano_terapeutico)

                cursor.execute(sql, valores)
                db_connection.commit()
                print(f"✅ Sucesso! {prontuario} salvo")
            
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
    
    def salvar_evolucao(self, evolucao):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "INSERT INTO Evolucao(id_prontuario, id_profissional, data_atual, texto) VALUES (%s, %s, %s, %s)"
                valores = (evolucao.id_prontuario, evolucao.id_profissional, evolucao.data_atual, evolucao.texto)

                cursor.execute(sql, valores)
                db_connection.commit()
                print(f"✅ Sucesso! {evolucao} salva")
            
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


    def buscar_por_paciente(self, id_paciente):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Prontuario WHERE id_paciente = %s"
                cursor.execute(sql,(id_paciente,))
                resultado = cursor.fetchone()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()

    def buscar_por_diagnostico(self, diagnostico):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Prontuario WHERE diagnostico = %s"
                cursor.execute(sql,(diagnostico,))
                resultado = cursor.fetchall()
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()
        