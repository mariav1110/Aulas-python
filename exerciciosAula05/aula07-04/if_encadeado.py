import os 
os.system("cls")
#Exercicio:
# 1.Dado uma nota verficar se ela é valida ou não.
'''nota = float(input("Nota:"))
      #true and true 
if nota >= 0 and nota <= 10:
    print("Nota válida")
else:
    print("Nota inválida")


if nota >= 0: #true
    if nota <= 10:
        print("Nota válida")
    else:#nota>10
        print("Nota invalida")
else:#nota < 0 
    print("Nota inválida")


# 2. Dadas 3 notas, verificar e exibir qual é a de menor valor
nota1 = float(input("Nota 1 :")) #5
nota2 = float(input("Nota 2 :")) #8
nota3 = float(input("Nota 3 :")) #2

menor = nota1 #menor 5 

if nota2 < menor:
    menor = nota2

if nota3 < menor:
    menor = nota3

print(menor)
'''

 # 3. Dadas 3 notas,calcular a media das duas maiores verificando se as notas são válidas.
import os 
os.system("cls")
nota1 = float(input("Nota 1 :"))
if nota1 >= 0 and nota <= 10:
    nota2 = float(input("Nota 2 :"))
    if nota2 >= 0 and nota <= 10:
       nota3 = float(input("Nota 3 :"))
       if nota3 >= 0 and nota <= 10:
           #se chegou aq todas as notas sao validas e pode calcular a media 
        menor = nota1 
        if nota2 < menor:
           menor = nota2
           if nota3 < menor:
              menor = nota3

       media = (nota1 + nota2 + nota3 - menor)/2

print(f"A média das duas maiores notas entre:{nota1:2f},{nota2:2f},{nota3:2f}")


#ler o numero
n= int(input("numero:"))
#calcular o quadrado do numero
q= n ** 2
#exibir o resultado
print(q)