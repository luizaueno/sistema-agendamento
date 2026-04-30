class LoginResponseDTO:
    def __init__(self, token, tempo_expiracao, perfil):
        self.token: int = token
        self.tempo_expiracao: int = tempo_expiracao
        self.perfil: str = perfil
        
