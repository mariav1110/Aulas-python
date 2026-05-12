salario = 1000

# maior 5000 -> 10% | até 5000 -> 5%
inss =  salario * 0.1 if salario > 5000 else salario * 0.05

print(salario, inss)