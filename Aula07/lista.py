import os
os.system("clear")

# Lista
# - conteudo heterogêneo (quaisquer tipos)
# - Tamanho dinâmico (pode mudar na execução do programa)

# Inicializar uma lista com valores
lista = ["Edson", 45, 3.2, True, 66]

print(lista)

for indice in range(0, 5, 1):
    print(f"V[{indice}] = {lista[indice]}")

for elemento in lista:
    print(elemento)

os.system("clear")

# Métodos de manipulação de lista
# list() - inicializa uma lista como vazia
os.system("clear")
lista = [] # ou list()
print(lista)


# append(elemento) - acrescenta um elemento no final da lista
os.system("clear")
lista = list()
lista.append("Edson")
lista.append(12)
lista.append(4.5)
lista.append(False)
# elemento = input("Elemento: ")
lista.append(elemento)
print(lista)

# insert(indice, elemento) - insere um elemento em uma posicao especifica
os.system("clear")
lista = [34, "Ester", 5.5, True, 55]
print(lista)
lista.insert(1, "Novo")
print(lista)

# pop(<indice>) - remove um elemento da lista () remove o ultimo | (indice) remove o indice
os.system("clear")
lista = [34, "Ester", 5.5, True, 55]
print(lista)
lista.pop() # remove o último
removido = lista.pop(0) # remove o elemento contido no índice 0
print(lista)
print(removido)

# remove(elemento) - remove o elemento especificado
os.system("clear")
lista = [34, "Ester", 5.5, True, 55]
print(lista)
lista.remove("Ester") # cuidado com elemento que nao existe
print(lista)

# index(elemento) - Retora o índice do elemento especificado
os.system("clear")
lista = [34, "Ester", 5.5, True, 55]
print(lista)
indice = lista.index(True) # cuidado com elemento inexistente
print(indice)

# count(elemento) - conta elementos especificados
os.system("clear")
lista = [34, "Ester", 5.5, True, 55, 34, 34]
print(lista)
elemento = 34
qtd = lista.count(elemento)
print(f"Existe {qtd} {elemento} na lista")

# Exemplo de aplicação
os.system("clear")
lista = [34, "Ester", 5.5, True, 55]
print(lista)
elemento = "Joao"
if lista.count(elemento) == 0:
    print(f"O elemento {elemento} não existe na lista!")
else: 
    indice = lista.index(elemento) # cuidado com elemento inexistente
    print(f"O elemento {elemento} está na posicao {indice}")

#

 