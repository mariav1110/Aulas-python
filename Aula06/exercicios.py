# EXERCICIOS:
# 1. Dados os numeros do intervalo, exiba o intervalo aberto
# (sem o inicio e sem o fim).
# ENTRADA: 2 9          SAÍDA: 3 4 5 6 7 8

# - ler a entrada - NÃO
inicio = int(input("Inicio:"))
# - Ler a saida - NÃO
fim = int(input("Fim:"))
# O laço começa em inicio + 1 para ser intervalo aberto
for volta in range(inicio , fim):
    print(volta, end=" ")

# --------OU--------------
#Inicio += 1     # inicio = inicio + 1 
#for volta in range(inicio + 1, fim):
   # print(volta, end=" ")


# 2. Dados 2 numeros do intervalo e o incremento, exiba os números de acordo
# com os parâmetros:
# ENTRADA: 4 20 3       SAÍDA: 4 7 10 13 16 19
inicio = int(input("Inicio :"))
fim = int(input("Fim:"))
incr = int(input("Incremento:"))
for volta in range(inicio,fim + 1,incr):
    print(volta,end=" ")