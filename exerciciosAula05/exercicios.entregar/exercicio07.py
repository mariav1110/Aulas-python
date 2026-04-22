#ler as notas
nota1 = int(input("Nota 1:"))
nota2 = int(input("Nota 2:"))

media = (nota1 + nota2) / 2

if media < 5:
    print("Média", media, "- Reprovado")
else:
    print("Média", media, "- Aprovado")