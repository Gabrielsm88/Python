#IF SIMPLES
#VARIAVEL
salario = novosal = 0.0

#INPUT
salario = float(input("Digite o salário atual: R$"))

#PROCESSAMENTO
if(salario < 500):
    novosal = salario * 0.15
elif(salario <= 1000):
    novosal = salario * 0.10
else:
    novosal = salario * 0.05

#OUTPUT
print(f"O novo salário é: R${novosal:.2f}")
