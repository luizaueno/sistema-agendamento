import bcrypt

class SenhaUtil:
    @staticmethod
    def hash (senha: str) -> str: # texto para hash
        senha_bytes = senha.encode('utf-8')
        salt = bcrypt.gensalt() # para não fazer hashs iguais ao digitar a senha
        hash = bcrypt.hashpw(senha_bytes, salt)
        return hash.decode('utf-8')

    @staticmethod
    def verificar(senha: str, hash: str) -> bool:
        user_bytes = senha.encode('utf-8')
        hash_bytes = hash.encode('utf-8')
        resultado = bcrypt.checkpw(user_bytes, hash_bytes)
        return resultado