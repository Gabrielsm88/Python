#VARIÁVEIS
salario1 = 0.0
salario2 = 0.0

#INPUT
salario1 = float(input("Digite o valor do salário: R$"))

#OUTPUT 
if salario1 < 2000:
    salario2 = salario1*1.10
    print(f"Seu salário era de: R${salario1}, agora é de: R${salario2}")
else:
    salario2 = salario1
    print(f"Seu salário é de: R${salario1} e continua sendo de: R${salario2:.2f}")
