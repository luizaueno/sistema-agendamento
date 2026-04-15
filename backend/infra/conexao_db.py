import mysql.connector # Aqui Zchama o tradutor que o pip instalou
import os # biblioteca do sistema para ler pastas e arquivos
from dotenv import load_dotenv 

load_dotenv() # le o .env da raiz

def criar_conexao():  # onde o Python estabelce conexao com o  MySQL
    db_connection = None
    try:
        db_connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )

        # Verificação lógica: a porta abriu?
        if db_connection.is_connected():
            print("✅ Conexão via .env estabelecida com sucesso!")
            return db_connection # Entrega a conexao pronta ao repository

    except Exception as e:
        # Se der erro (senha errada, banco desligado), ele cai aqui
        print(f"Ops! Não consegui conectar. O erro foi: {e}")
        return None