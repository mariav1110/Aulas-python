#2. Média de números
#Dados 5 números pelo usuário, exiba a média.
##Exemplo de Entrada: 10, 5, 3, 2, 10
#Exemplo de Saída: 6

soma = 0 #inicia a variavel

# O range(1, 6, 1) vai rodar para os valores 1, 2, 3, 4 e 5 (total de 5 vezes)
for cont in range(1, 6, 1):
    n = int(input("Digite um número: "))
    soma = soma + n 
    media = soma / 5

print(media)
