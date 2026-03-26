# Buscar paciente por id
def busca_binaria(vetor, id_procurado):
    indice = 0
    inicio = 0
    fim = len(vetor) -1
    while (inicio <= fim):
        meio = (inicio + fim) // 2
        if vetor[meio] > id_procurado:
            fim = meio -1
        elif vetor[meio] < id_procurado:
            inicio = meio + 1
        else:
            return meio

            
entrada = input("Digite a lista de IDs separados por espaço: ")
vetor = [int (x) for x in entrada.split()]
id_procurado = int(input("Digite o ID procurado: "))
if(busca_binaria(vetor, id_procurado) != None):
    print(f"O ID procurado está na posição {id_procurado} do vetor ")
else: 
    print(f"O ID procurado não está no vetor ")