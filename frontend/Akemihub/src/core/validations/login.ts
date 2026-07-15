export function validarEmail(email: string): string  {
   
    if (email === '') {
        return "Informe um email"
    }

    else {
        return "Email não cadastrado"
    }

}

export function validarSenha(senha: string): string {
    if (senha == '') {
        return "Informe uma senha"
    }
    
    else {
        return "Senha incorreta. Tente de novo"
    }
}
