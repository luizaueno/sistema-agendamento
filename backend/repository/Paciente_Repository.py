from infra.conexao_db import criar_conexao

class PacienteRepository:
    def salvar(self, paciente):
        db_connection = criar_conexao()

        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True) # é quem realmente executa os comandos sql no banco - entre o python e o banco, se usa dicionario para acesar o nome de cada dado
                sql = "INSERT INTO Paciente(nome, data_nascimento, sexo, nome_responsavel, cpf, telefone, id_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (paciente.nome, paciente.data_nascimento, paciente.sexo, paciente.nome_responsavel, paciente.cpf, paciente.telefone, paciente.id_empresa)

                cursor.execute(sql, valores)
                db_connection.commit()
                print(f"✅ Sucesso! {paciente} salvo")

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

    
    def buscar_por_cpf(self, cpf):
        db_connection =  criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Paciente WHERE cpf = %s"
                cursor.execute(sql,(cpf,))
                resultado = cursor.fetchone() # traz o resultado do banco
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()


    def buscar_por_responsavel(self, nome_responsavel):
        db_connection = criar_conexao()
        if db_connection:
            try:
                cursor = db_connection.cursor(dictionary=True)
                sql = "SELECT * FROM Paciente WHERE nome_responsavel = %s"
                cursor.execute(sql,(nome_responsavel,))
                resultado = cursor.fetchall() # varios pacientes com um responsavel
                return resultado
            except Exception as e:
                print(f"Erro ao buscar no banco: {e}")
                return None
            finally:
                if db_connection.is_connected():
                    cursor.close()
                    db_connection.close()