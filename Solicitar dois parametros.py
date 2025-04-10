#Solicitar dois parametros
#laço de repetição para solicitar 10 numeros
#verificar quantos estão abaixo do primeiro e acima do segundo
 
    
import os
os.system('cls')

while True:


 abaixo = acima = qtdAbaixo = qtdAcima = 0
    
 abaixo = int(input("Digite um número: "))
 acima = int(input("Digite outro número: "))

 for cont in range(10):
            num = int(input(f"Digite o {cont+1}º numero: "))
    
            if num <= abaixo:
             qtdAbaixo += 1
        
            if num >= acima:
                qtdAcima += 1
                
 print(f"Quantidade abaixo de {abaixo} = {qtdAbaixo}")
 print(f"Quantidade acima de {acima} = {qtdAcima}")

 rsp = input("Quer rodar novamente? (S/N): ")
 if rsp.upper() == 'N':
        break