# 1. Dada uma nota, informar se ela é válida ou nao (entre 0 e 10)

nota = float(input("Nota:"))
if nota  >= 0 and nota <= 10:
    #true and true (5)
    #false and true (-2)
    #true and false (56)
    print("Nota válida!")
else:
    print("Nota Invalida!")