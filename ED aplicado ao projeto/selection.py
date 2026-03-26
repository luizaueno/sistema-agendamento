def select(vetor):
    for posicao_atual in range(len(vetor)):
        indice_min = posicao_atual
        for indice in range(posicao_atual+1, len(vetor)):
            if vetor[indice] < vetor[indice_min]:
                indice_min = indice
            aux = vetor[indice_min]
            vetor[indice_min] = vetor[posicao_atual]
            vetor[posicao_atual] = aux

    return vetor


entrada = input("Digite os IDs separados por espaço: ")
vetor = [int (x) for x in entrada.split()]
print(f"Vetor original: {entrada}")
select(vetor)
print(f"Horários ordenados {vetor}")