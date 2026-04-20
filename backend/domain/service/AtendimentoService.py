from datetime import date
from domain.entities import Paciente, Profissional, Atendimento
from domain.exceptions import CampoObrigatorioVazio, StatusInvalido, HorarioIndisponivel, PacienteInexistente, ProfissionalInexistente, DataIndisponivel

class AtendimentoService:
    def __init__(self, atendimento_repository, paciente_repository, profissional_repository):
        self.repo_atendimento = atendimento_repository
        self.repo_paciente = paciente_repository
        self.repo_profissional = profissional_repository
    
    def cadastrar(self, id_paciente, id_profissional, status, data, hora_inicio, hora_fim):

        if not id_paciente or not id_profissional or not status or not data or not hora_inicio or not hora_fim:
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
        
        paciente_id = self.repo_paciente.get_by_id(id_paciente)
        if not paciente_id:
            raise PacienteInexistente("Esse paciente não está cadastrado no sistema")
      
        profissional_id = self.repo_profissional.get_by_id(id_profissional)
        if not profissional_id:
            raise ProfissionalInexistente("Esse profissional não está cadastrado no sistema")
        
        if data < date.today():
            raise DataIndisponivel("Data indisponível")
        
        valores_status = ["AGENDADO", "CANCELADO", "CONFIRMADO", "REALIZADO"]
        if status not in valores_status:
            raise StatusInvalido("Esse status não está disponível")
        
        disponibilidade_atend = self.repo_atendimento.verificar_disponibilidade(id_profissional, data, hora_inicio, hora_fim)
        if disponibilidade_atend:
            atendimento_novo = Atendimento(id_paciente, id_profissional, status, data, hora_inicio, hora_fim)
            self.repo_atendimento.salvar(atendimento_novo)
        else:
            raise HorarioIndisponivel("Esse horário não está disponivel na data agendada")
    
    def buscar_por_paciente(self, id_paciente):
        paciente_id = self.repo_paciente.get_by_id(id_paciente)
        if not paciente_id:
            raise PacienteInexistente("Esse paciente não está cadastrado no sistema")
        atendimentos_paciente = self.repo_atendimento.buscar_por_paciente(id_paciente)
        return atendimentos_paciente
    
    def buscar_por_profissional(self, id_profissional):
       profissional_id = self.repo_profissional.get_by_id(id_profissional)
       
       if not profissional_id:
            raise ProfissionalInexistente("Esse profissional não está cadastrado no sistema")
       atendimentos_profissional = self.repo_atendimento.buscar_por_profissional(id_profissional)
       return atendimentos_profissional

    def buscar_por_data(self, data):
        if data is None:
            raise CampoObrigatorioVazio("Selecione uma data para o atendimento")
        atendimentos_data = self.repo_atendimento.buscar_por_data(data)
        return atendimentos_data

    def buscar_por_status(self, status):
        valores_status = ["AGENDADO", "CANCELADO", "CONFIRMADO", "REALIZADO"]
        if status in valores_status:
            status_valido = self.repo_atendimento.buscar_por_status(status)
            return status_valido
        raise StatusInvalido("Esse status não está disponível")