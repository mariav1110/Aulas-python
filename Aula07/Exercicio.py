#exercicio 1

# Fazer um programa que inicialize uma lista vazia.
# Peça para o usuário digitar elementos até que seja digitado '.''
# Exibir o conteudo da lista
# v2.0 - Depois de mostrar a lista, colocar em uma lista somente os dados inteiros e na outra os 
# demais dados
# ['Edson', '33', '23', '21', '95', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']
# lista inteiros = [33, 23, 21, 95]
# lista outros = ['Edson', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']

"""
Digite elementos:
34
67
Maria
True
.
lista = [34, 67, 'Maria', True]
"""

lista = list()

while True:
    elem = input("Elemento: ")
    if elem == '.':
        break
    else:
        lista.append(elem)

print(lista)