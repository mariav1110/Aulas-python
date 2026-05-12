#ler o número
numero = int(input("Digite o número:"))
if numero % 5 != 0 :
    numero2 = numero + (5 - numero % 5)
    print(numero2)
else:
    print(numero)
