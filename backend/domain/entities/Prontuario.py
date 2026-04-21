class Prontuario:
    def __init__(self, id_paciente, diagnostico, plano_terapeutico, id=None):
        self.id: int = id
        self.diagnostico: str = diagnostico
        self.plano_terapeutico: str = plano_terapeutico
        self.id_paciente: int = id_paciente
        