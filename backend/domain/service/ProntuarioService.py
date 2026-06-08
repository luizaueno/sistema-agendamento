from domain.entities import Paciente, Evolucoes, Prontuario
from domain.exceptions import CampoObrigatorioVazio, IdInvalido, ProntuarioExistente

class ProntuarioService:
    def __init__(self, paciente_repository, prontuario_repository):
        self.repo_paciente = paciente_repository
        self.repo_prontuario = prontuario_repository
        
    def cadastrar(self, id_paciente, diagnostico, plano_terapeutico):
        if not id_paciente or not diagnostico or not plano_terapeutico:
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")

        paciente_id = self.repo_paciente.get_by_id(id_paciente)
        if not paciente_id:
            raise IdInvalido("Esse paciente não está cadastrado no sistema")
        
        id_prontuario = self.repo_prontuario.prontuarioexistente(id_paciente)
        if id_prontuario is not None:
            raise ProntuarioExistente("Esse paciente já tem um prontuário")
        
        prontuario_novo = Prontuario(id_paciente, diagnostico, plano_terapeutico)
        self.repo_prontuario.salvar(prontuario_novo)

    def salvar_evolucao(self, id_prontuario, id_profissional, data_atual, texto):
        if not id_prontuario or not id_profissional or not data_atual or not texto:
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")

        evolucao_nova = Evolucoes(id_prontuario, id_profissional, data_atual, texto)
        self.repo_prontuario.salvar_evolucao(evolucao_nova)

    def buscar_por_paciente(self, id_paciente):
        paciente_id = self.repo_paciente.get_by_id(id_paciente)
        if not paciente_id:
            raise IdInvalido("Esse paciente não está cadastrado no sistema")
        paciente = self.repo_prontuario.buscar_por_paciente(id_paciente)
        return paciente
    
    def buscar_por_diagnostico(self, diagnostico):
        if not diagnostico:
            raise CampoObrigatorioVazio("Campo Obrigatorio não preenchido")
        diagnostico = self.repo_prontuario.buscar_por_diagnostico(diagnostico)
        return diagnostico