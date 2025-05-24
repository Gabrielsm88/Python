#IF ENCADEADO
#VARIAVEL
salario = novosal = 0.0

#INPUT
salario = float(input("Digite o salário atual: R$"))

#PROCESSAMENTO
if(salario >= 500):
    if(salario > 1000):
        novosal = salario * 0.05
    else:
        novosal = salario * 0.10
else:
    novosal = salario * 0.15
    
#OUTPUT
print(f"O novo valor do salário é: R${novosal:.2f}")
