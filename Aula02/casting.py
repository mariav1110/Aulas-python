import os
os.system("clear") # Windows "cls"

# Casting - mudança de tipo da variável
conteudo = 45.7
print(conteudo, type(conteudo), conteudo + conteudo) #type mostra o status (tipo)
conteudo = int(conteudo)
print(conteudo, type(conteudo), conteudo + conteudo)
conteudo = str(conteudo)
print(conteudo, type(conteudo), conteudo + conteudo)
conteudo = bool(conteudo)
print(conteudo, type(conteudo), conteudo + conteudo)

# Operadores aritméticos
os.system("clear") # Windows "cls"
n1 = 10
n2 = 3
resp = n1 + n2
print(resp, type(resp))
resp = n1 - n2
print(resp, type(resp))
resp = n1 * n2
print(resp, type(resp))
resp = n1 / n2
print(resp, type(resp),type(n1),type(n2))
resp = n1 // n2 # Divisão inteira
print(resp, type(resp))
resp = n1 % n2 # módulo -> resto da divisão
print(resp, type(resp))

n1 = 17
n2 = 7
resp = n1 // n2 # Divisão inteira
print(resp, type(resp))
resp = n1 % n2 # módulo -> resto da divisão
print(resp, type(resp))

n1 = 12.5
n2 = 5.1
resp = n1 // n2 # Divisão inteira
print(resp, type(resp))
resp = n1 % n2 # módulo -> resto da divisão
print(resp, type(resp))
"""
_ 12.5 | 5.1
  10.2     2
   2.3   
"""
n1 = 15
n2 = 4
resp = n1 + n1 * n2 / 2 - n2
#      15 + 15 * 4  / 2 - 4
#      15 + 60 / 2 - 4
#      15 + 30 - 4
#      45 - 4
#      41
print(resp)
resp = n1 % n1 // n2 / n1 * n2
#      15 % 15 // 4  / 15 * 4
#      0       // 4  / 15 * 4
#      0 / 15 * 4
#      0 * 4
#      0
print(resp)

resp = 3 ** 4 # Exponenciação
print(resp)

resp = (n1 + n1) * n2 / (2 - n2)
print(resp)

# operadores literais (texto)
resp = "34" + "34"
print(resp)
n1 = "34"
n2 = "4"
resp = n1 * 4
print(resp)