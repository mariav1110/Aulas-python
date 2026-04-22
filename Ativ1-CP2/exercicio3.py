# 3. Múltiplos
# Dado um número pelo usuário, exiba os seus 10 múltiplos a partir dele.
# Exemplo de Entrada: 5
# Exemplo de Saída: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

n = int(input("Digite um número:"))

for volta in range(1,11,1):
    multiplo = n * 5
    print(volta,end=" ")