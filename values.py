#VARIAVEIS
salario = 0.0
salarioliq = 0.0
convenio = 0.0
inss = 0.0
irrf = 0.0

#INPUT
salario = float(input("Digite o valor do salário: R$"))
convenio = float(input("Digite o valor gasto em farmácia: R$"))

#CÁLCULOS
convenio = convenio*0.8
inss = salario*0.08
irrf = salario*0.11
salarioliq = salario - inss - irrf - convenio

#OUTPUT
print(f"O valor do salário líquido é: R${salarioliq}")
print(f"O valor do convênio é: R${convenio}")
print(f"O valor do INSS é: R${inss}")
print(f"O valor do IRRF é: R${irrf}")
