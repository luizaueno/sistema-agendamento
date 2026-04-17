from domain.entities import Paciente, Profissional
from domain.exceptions import CampoObrigatorioVazio, StatusInvalido, HorarioIndisponivel, PacienteInexistente, ProfissionalInexistente, DataIndisponivel

class AtendimentoService:
    def __init__(self, atendimento_repository, paciente_repository, profissional_repository):
        self.repo_atendimento = atendimento_repository
        self.repo_paciente = paciente_repository
        self.repo_profissional = profissional_repository
    
    def cadastrar(self, id_paciente, id_profissional, status, data, hora_inicio, hora_fim):

        if not id_paciente or not id_profissional or not status or not data or not hora_inicio or not hora_fim:
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
        
        resultado = self.repo_paciente.get_by_id(id_paciente)
        if not resultado:
            raise PacienteInexistente("Esse paciente não está cadastrado no sistema")
      
        resultado = self.repo_profissional.get_by_id(id_profissional)
        if not resultado:
            raise ProfissionalInexistente("Esse profissional não está cadastrado no sistema")
        

        