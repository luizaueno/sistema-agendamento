from pydantic import BaseModel, field_validator
from domain.exceptions import NomeInvalido, CampoObrigatorioVazio, CnpjInvalido, EmailInvalido, SenhaInvalida
from utils.limpar_cnpj import limpar_cnpj

class CadastroDTO(BaseModel):
    nome: str
    cnpj: str
    email_empresa: str
    senha: str

    @field_validator('nome')
    def validar_nome(nome):
        nome = nome.strip()
        if nome == "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        if len(nome) < 5:
            raise NomeInvalido("O nome da sua empresa precisa ser maior")
        return nome
    
    @classmethod
    @field_validator('cnpj', mode="before") # aceita dados sujos e tem a função de limpar
    def validar_cnpj(cls, v):
        if not isinstance(v, str):
            raise CnpjInvalido("Formato do cnpj incorreto")
        cnpj_limpo = limpar_cnpj(v)
        if cnpj_limpo == "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        if len(cnpj_limpo) != 14:
            raise CnpjInvalido("O tamanho do CNPJ está incorreto")
        return cnpj_limpo
 
    @classmethod # acessa e modifica atributos da classe
    @field_validator('email_empresa')
    def validar_email(cls, v): # pertence a classe CadastroDTO, e o v é o valor bruto
        v = v.strip()
        v = v.lower()
        if v == "":
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
        email = v.split("@")
        if len(email) != 2 or "." not in email[1]:
            raise EmailInvalido("O formato do email está incorreto")
        return v
 
    @classmethod
    @field_validator('senha')
    def validar_senha(cls, v):
        v = v.strip()
        if v == "":
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
        if len(v) < 8:
            raise SenhaInvalida("A senha precisa de no mínimo 8 caracteres")
        if not any(char.isupper() for char in v) or not any(char.islower() for char in v):  # char in v seria cada digito, no v, a string inteira
            raise SenhaInvalida("A senha precisa ter ao menos uma letra maiúscula e outra minúscula")
        if not any(char.isdigit() for char in v) or not any(char.isalnum() for char in v):
            raise SenhaInvalida("A senha precisa ter ao menos um número e um caractere especial")
        return v
