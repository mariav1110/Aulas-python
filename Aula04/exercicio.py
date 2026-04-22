# Exercício:
# A partir de uma compra, o usuário terá um desconto.
# - Se a compra for acima de 1000 reais, terá um desconto de 10%
# - Se a compra for entre (inclusive) 500 e 1000, terá um desconto de 5%
# - Se a compra for abaixo de 500, não terá desconto.
# Ao finalizar exiba: O valor da compra, o valor do desconto e o valor da compra
# com o desconto

#Algoritimo
#-Digitar a compra
compra = float(input("Compra:"))
#-Se a compra for a cima de 1000
# desconto de 10%
if compra > 1000:
    desconto = compra * 0.10
#-Se a compra for entre 500 e 100, desconto 5%
elif compra >= 500 and compra <= 1000:
    desconto = compra * 0.05
#Se a compra for menor que 500,nao tem desconto
else:
    desconto = 0 
com_desconto = compra - desconto 

print(f"""
      Compra............: R${compra:10.2f}
      Desconto ..........: R#{desconto:10.2f}
      compra c/ desconto..: R$ {com_desconto:10.2f}""")