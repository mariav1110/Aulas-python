


# - ler o valor inicial - NÃO
inicio = int(input("Valor inicial:"))
# - Ler  o valor final - NÃO
fim = int(input("Valor final:"))

for volta in range(inicio,fim + 1,1):
#-----------------------------------
# - Exibir os números - SIM
    print(volta, end = " ")
# - Somar 1 para o próximo número - SIM
#--------------------------------------
print()
for volta in range(1,11,1):
    print(volta, end= " ")

print()

inicio = 1 
while inicio <= 10:
    print(inicio,end = " ")
    inicio = inicio + 1