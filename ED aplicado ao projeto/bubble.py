# Ordene esse array ["14:00", "09:00", "11:00", "08:00", "10:00", "15:00"]

def bubble(vetor):
    for passagem in range(len(vetor)):
        for indice_atual in range(len(vetor) -1):
            if vetor[indice_atual] > vetor[indice_atual +1]:
                aux = vetor[indice_atual]
                vetor[indice_atual] = vetor[indice_atual + 1]
                vetor[indice_atual +1] = aux



entrada = input("Digite os horários separados por espaço: ")
vetor = [int(x) for x in entrada.split()]
print(f"Valores de entrada {entrada}")
bubble(vetor)
print(f"Grade organizada {vetor}")