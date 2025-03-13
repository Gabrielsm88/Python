#VARIAVEL
salario = 0.0

#INPUT
salario = float(input("Digite o salário atual: R$"))

#PROCESSAMENTO
if(salario >= 500):
    if(salario > 1000):
        salario = salario + (salario * 0.05)
        print(f"O novo valor do salário é: R${salario:.2f}")
    else:
        salario = salario + (salario * 0.10) 
        print(f"O novo valor do salário é: R${salario:.2f}")
else:
    salario = salario + (salario * 0.15)
    print(f"O novo valor do salário é: R${salario:.2f}")