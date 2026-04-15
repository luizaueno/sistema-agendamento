from datetime import time, date
from enum import Enum

class StatusEnum(Enum):
    AGENDADO = "Agendado"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"
    REALIZADO = "Realizado"

class Atendimento:
    def __init__(self, id_paciente, id_profissional, status, data, hora_inicio, hora_fim, id=None):
        self.id: int = id
        self.id_paciente: int = id_paciente
        self.id_profissional: int = id_profissional
        self.status: StatusEnum = status
        self.data: date = data
        self.hora_inicio: time = hora_inicio
        self.hora_fim: time = hora_fim
  