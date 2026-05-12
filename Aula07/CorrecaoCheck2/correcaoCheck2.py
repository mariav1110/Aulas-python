import os
os.system("clear")

# Digitação dos nomes dos candidatos (não em branco)
print("Digite os nomes dos candidatos: ")
nome_cand1 = input("1: ")
while nome_cand1 == "":
    nome_cand1 = input("Nome em branco, digite algo!\n1: ")

nome_cand2 = input("2: ")
while nome_cand2 == "":
    nome_cand2 = input("Nome em branco, digite algo!\n2: ")

nome_cand3 = input("3: ")
while nome_cand3 == "":
    nome_cand3 = input("Nome em branco, digite algo!\n3: ")

# Inicialização multipla
voto_cand1 = voto_cand2 = voto_cand3 = voto_nulo = total_votos = 0

# Exibir o menu
print(f"""
CANDIDATOS

1 - {nome_cand1}
2 – {nome_cand2}
3 – {nome_cand3}
0 – FIM DA VOTAÇÃO 

""", end = "")

while True:
    voto = input("VOTO: ")
    match voto:
        case '0':
            break
        case '1':
            voto_cand1 = voto_cand1 + 1
        case '2':
            voto_cand2 += 1 # x *= 2
        case '3':
            voto_cand3 += 1
        case _:
            print("Votou nulo!")
            voto_nulo += 1
    
    total_votos += 1

# Calcular os percentuais
perc_cand1 = voto_cand1 / total_votos * 100
perc_cand2 = voto_cand2 / total_votos * 100
perc_cand3 = voto_cand3 / total_votos * 100
perc_nulo = voto_nulo / total_votos * 100

# Apuração
print(f"""
CANDIDATOS
TOTAS DE VOTOS: {total_votos}
1 – {nome_cand1:12s} -> {voto_cand1:3d} votos -> {perc_cand1:5.1f}%
2 – {nome_cand2:12s} -> {voto_cand2:3d} votos -> {perc_cand2:5.1f}%
3 – {nome_cand3:12s} -> {voto_cand3:3d} votos -> {perc_cand3:5.1f}%
    {"NULOS":12s} -> {voto_nulo:3d} votos -> {perc_nulo:5.1f}% 
""")








"""
x = 0
x = x + 1 # acumuladora: usa ela mesma no calculo | deve ser inicializada
"""

 