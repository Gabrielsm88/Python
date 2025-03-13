#VARIAVEIS
salarioliq = salariobrt = ir = inss = 0.0

#INPUT
salariobrt = float(input("Digite o salário bruto: R$"))

#Processamento
if(salariobrt < 1500):
    irrf = 0
    inss = salariobrt * 0.08
else:
    irrf = salariobrt * 0.05
    inss = salariobrt * 0.11
    
salarioliq = salariobrt - irrf - inss

#OUTPUT
print(f"Salario Bruto.............: {salariobrt:10.2f}")
print(f"INSS......................: {inss:10.2f}")
print(f"IRRF......................: {irrf:10.2f}")
print(f"Salario Liquido...........: {salarioliq:10.2f}")