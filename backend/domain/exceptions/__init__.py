

# 1. As compartilhadas vêm do arquivo NOVO (herdando de ValueError)
from .SharedExeptions import (
    CampoObrigatorioVazio,
    NomeCurto, 
    EmailInvalido,
    CnpjInvalido, 
    SenhaInvalida, 
    EspecialidadeInvalida, 
    TelefoneInvalido,
    CorInvalida
)

# 2. As específicas de Empresa vêm do arquivo de Empresa (herdando de Exception)
from .EmpresaExceptions import (
    EmpresaNaoEncontrada, 
    LimiteAdmins,
    CnpjJaCadastrado
)

# 3. As específicas de Usuário vêm do arquivo de Usuário (herdando de Exception)
from .UsuarioExceptions import (
    UsuarioNaoEncontrado,
    EmailJaCadastrado
)
