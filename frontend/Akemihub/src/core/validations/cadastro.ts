export function validarNome(nome: string): string {
    if (nome == '') {
        return "Informe o nome da empresa"
    }
    else if (nome.length < 5) {
        return "O nome da empresa precisa de pelo menos 5 letras"
    }
    else {
        return ""
    }
}

export function validarCNPJ(cnpj_sujo: string): string {
    const cnpj_limpo = cnpj_sujo.replace(/[^0-9]/g, "")
    if (cnpj_limpo == '') {
        return "Informe um CNPJ"
    }
    else if (cnpj_limpo.length < 14) {
        return "O CNPJ da empresa precisa de 14 digitos"
    }
    else {
        return ""
    }
}

export function validarEmail(email: string): string | null {
   
    if (email === '') {
        return "Informe um email"
    }

    const email_dividido = email.split("@")

    if (email_dividido.length !== 2 || !email_dividido[1].includes(".") || email_dividido[1].length < 6) {
        return "Formato incorreto do email"
    }

    // Corrigido: adicionado [0][0] para verificar a primeira letra antes do @
    if (!email_dividido[0] || !/[a-zA-Z]/.test(email_dividido[0][0])) {
        return "Email deve começar com letra"
    }

    return null

}

export function validarSenha(senha: string): string {
    if (senha == '') {
        return "Informe uma senha"
    }
    else if (senha.length < 8) {
        return "A senha precisa de 8 digitos"
    }

    else if (!/[A-Z]/.test(senha) || !/[a-z]/.test(senha)) {
        return "A senha precisa ter ao menos uma letra maiúscula e outra minúscula"
    }
    else if (!/[0-9]/.test(senha) || !/[^a-zA-Z0-9]/.test(senha)) {
        return "A senha precisa ter ao menos um número e um caractere especial"
    }
    else {
        return ""
    }
}
