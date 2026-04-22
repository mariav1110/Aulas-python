def meu_maxs2(l: list) -> int:
    maior = lista[1]

    for i in range(2, len(lista)-1, 1):
        if lista[i] > maior:
            maior = lista[i]

    return(maior)



# LÓGICA DE PROGRAMAÇÃO

lista = [45, 23, 67, 23, 12]

maior = lista[1]

for i in range(2, len(lista)-1, 1):
    if lista[i] > maior:
        maior = lista[i]

print(maior)

# DANADINHO
lista = [45, 23, 67, 23, 12]
maior = max(lista)
print(maior)

maior = meu_maxs2(lista)
print(maior)

