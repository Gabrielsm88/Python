#Nao específica valores iguais

A = B = C = 0.0

#INPUT
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

#PROCESSAMNETO
if(A > B):
    if(A > C):
        print(f"O valor de A é o maior = {A}")
    else:
        print(f"O valor de C é o maior = {C}")
else:
    if(B > C):
        print(f"O valor de B é o maior: = {B}")
    else:
        print(f"O valor de C é o maior: = {C}")