import os
os.system("clear") # "cls"
# 3. Fazer um algoritmo que calcule a média de 4 números dados pelo usuário. 
"""
# NARRATIVA - ALGORTIMO
# - Digitar o 1.o numero (ED) - input()
n1 = input("1.o Número: ") # input() lê dado string
n1 = float(n1) # Casting - Mudar o tipo do dado

# - Digitar o 2.o numero (ED) - input()
n2 = float(input("2.o Número: ")) # input() com o casting

# - Digitar o 3.o numero (ED) - input()
n3 = float(input("3.o Número: ")) # input() com o casting

# - Digitar o 4.o numero (ED) - input()
n4 = float(input("4.o Número: ")) # input() com o casting

# - Calcular a média de 4 numero - Calculos (operadores aritm.)
media = (n1 + n2 + n3 + n4) / 4

# - Exibir a média (SD) - print()
print(f"Média = {media:.1f}")
"""
# 5. Dada a quilometragem parcial de um carro (km) e a quantidade de litros (l) gastos para percorrer esta
# quilometragem, fazer um algoritmo que calcule quantos Km/l o carro percorreu
"""
# NARRATIVA - algoritmo
# - Digitar a distancia percorrida em km (ed)
km = float(input("Kilometragem percorrida: "))
# - Digitar a qtd de litros gastos (ed)
litros = float(input("Litros gastos: "))
# - Calcular o consumo medio do carro (pd)
consumo = km / litros
# - Exibir o consumo (sd)
print(f"Kilometragem: {km} \nLitros gastos: {litros} \nConsumo: {consumo:.2f}")
"""
"""
Dado o preço do maço de cigarros (preco), a quantidade de
maços consumidos por dia (q_m_d) e o tempo em anos
(anos) que a pessoa fuma, calcular quanto esta pessoa já
gastou fumando.

preco = 12
q_m_d = 1.5 # dias
tempo = 3 # anos
dias_fumo = tempo * 365
gasto = dias_fumo * q_m_d * preco
"""


