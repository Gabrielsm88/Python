#65 - M/F   

nome = sexo = ""
qtdP = qtdMASC = qtdFEM = 0
porcMASC = porcFEM = 0.00

while True:
    
    nome = input("Qual o seu nome? ")
    
    while True:
        sexo = input("Informe o seco biológico (M/F): ").upper()
        if sexo == "M" or sexo == "F":
            break
        
    qtdP += 1
    if sexo == "M":
        qtdMASC += 1
    else:
        qtdFEM += 1
    
    rsp = input("Digitar mais pessoas (S/N) ?")
    if rsp.upper() == 'N':
        break
    
porcFEM = qtdFEM / float(qtdP) * 100
porcMASC = qtdMASC / float(qtdP) * 100

print(f"Total de pessoas cadastradas...................: {qtdP}")
print(f"Total de pessoas do sexo masculino...................: {qtdMASC}")
print(f"Total de pessoas do sexo feminino...................: {qtdFEM}")
print(f"Porcentagem de pessoas do sexo Masculino...................: {porcMASC:.2f}")
print(f"Porcentagem Total de pessoas do sexo Feminino...................: {porcFEM:.2f}")
