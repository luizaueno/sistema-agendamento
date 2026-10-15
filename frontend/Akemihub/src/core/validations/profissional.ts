import { validarCNPJ } from './cadastro'
import { validarEmail } from './login'

export function validarNome(nome: string): string | null {
    if (nome == '') {
        return "Informe o nome da(o) profissional"
    }

    else {
        return ""
    }
}

export function validarEspecialidade(nome: string): string | null {
    if (nome == '') {
        return "Informe a especialidade da(o) profissional"
    }

    else {
        return ""
    }
}

export function validarTelefone(telefone: string): string | null {
 
    const telefone_limpo = telefone.replace(/[^0-9]/g, "")

    if (telefone_limpo == '') {
        return "Informe o telefone da(o) profissional"
    }

    else if (telefone_limpo.length < 11) {
        return "O Telefone da profissional precisa de 11 digitos"
    }
    else {
        return ""
    }

}

export { validarCNPJ, validarEmail }
