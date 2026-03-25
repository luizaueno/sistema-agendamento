# Busque marina_siva numa lista de nomes [sofia_andrade, fabricio_mendes, luiza_ueno, alanna_lacerda marina_ silva marina_silva]

def busca_linear(vetor, nome_procurado):
    # iB = indice de busca
    iB = 0 
    while (iB <= len(vetor) -1) and (nome_procurado != vetor[iB]):
        iB += 1
    return iB < len(vetor)


entrada = input("Digite os nomes separados por espaço: ")
vetor = entrada.split()
nome_procurado = input("Digite o nome a ser procurado")
if busca_linear(vetor, nome_procurado):
    print(f"O nome {nome_procurado} está na lista de pacientes")
else:
    print(f"{nome_procurado} não está na lista de pacientes")