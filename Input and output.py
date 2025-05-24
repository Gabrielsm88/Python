#criando variaveis
nome = "" #String
idade = 0 #Int
salario = 0.0 #Float

#entrada de dados
nome = input("digite seu nome: ") #Só devolve String
idade = int(input("Qual sua idade? ")) #para numeros é preciso fazerer a conversão com as funçoes int() e float()

salario = float(input("Qual seu salário: "))

#saida de dados
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"salário: R$ {salario}") #Não está formatado
print(f"Salário: R$ {salario:.2f}") #formatado com 2 casas decimais
