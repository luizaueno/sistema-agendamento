from datetime import date

class Evolucoes: 
    def __init__(self, id_prontuario, id_profissional, data_atual, texto, id=None):
        self.id: int = id
        self.data_atual: date = data_atual
        self.id_prontuario: int = id_prontuario
        self.id_profissional: int = id_profissional
        self.texto: str = texto
        