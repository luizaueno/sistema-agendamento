from pydantic import BaseModel, field_validator
from domain.exceptions import NomeInvalido, CampoObrigatorioVazio, CnpjInvalido, EmailInvalido

class CadastroDTO(BaseModel):
    nome: str
    cnpj: str
    email_empresa: str

    @field_validator('nome')
    def validar_nome(nome):
        nome = nome.strip()
        if nome == "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        return nome
    
    @field_validator('nome')
    def validar_tamanho_nome(nome):
        if len(nome) < 5:
            raise NomeInvalido("O nome da sua empresa precisa ser maior")
        return nome
    
    @field_validator('cnpj')
    def validar_tamanho_cnpj(cnpj):
        if cnpj == "":
              raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        
        cnpj = cnpj.strip()
        if len(cnpj) < 14:
            raise CnpjInvalido("O tamanho do CNPJ está incorreto")
        return cnpj
    
    @field_validator('email_empresa')
    def validar_email(email_empresa):
        if email_empresa == "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        
        if not "@" in email_empresa or not ".com" in email_empresa:
            raise EmailInvalido("O formato do email está incorreto")
        return email_empresa
