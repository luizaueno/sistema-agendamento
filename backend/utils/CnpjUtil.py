def limpar_cnpj(cnpj):
    cnpj_limpo = ""
    for c in cnpj:
        if c.isdigit():
            cnpj_limpo = cnpj_limpo + c
    return cnpj_limpo