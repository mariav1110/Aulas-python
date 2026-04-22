import os
os.system("clear") # Windows "cls"

nome = "Edson de Oliveira" # str()
idade = 51 # int()
altura = 1.71 # float()

# Forma 1 - convencional (usando vírgula) - acrescenta um espaço - aceita todos os tipos de dados
os.system("clear") # Windows "cls"
print(nome, idade, altura)
print("Nome:",nome, "Idade:",idade, "Altura:", altura) # \n - pula uma linha
print("\nNome:",nome, "\nIdade:",idade, "\nAltura:",altura) # \n - pula uma linha

# Forma 2 - Usando concatenação + (junção)
os.system("clear") # Windows "cls"
print(str(nome) + " " + str(idade) + " " +str(altura))
print("\nNome: " + nome + "\nIdade: " + str(idade) + "\nAltura: " +str(altura))

# Forma 3 - Usando a função format()
os.system("clear") # Windows "cls"
#                            0    1      2
print("{0} {1} {2}".format(nome, idade, altura))
print("\nNome: {0} \nIdade: {1} \nAltura: {2} - Nome: {0}".format(nome, idade, altura))
print("\nNome: {n} \nIdade: {i} \nAltura: {a} ".format(n=nome, i=idade, a=altura)) # alias

# Forma 4 - Usando f print
os.system("clear") # Windows "cls"
print(f"{nome} {idade} {altura}")
print(f"\nNome: {nome} \nIdade: {idade} \nAltura:{altura}")

os.system("clear") # Windows "cls"
print(f"Nome: {nome}") # print exibe e pula linha
print(f"Idade: {idade}")
print(f"Altura:{altura}")

# Tripo quotes ''' texto '''
print(f"""
Nome: {nome}
Idade: {idade}
Altura: {altura}
""")








