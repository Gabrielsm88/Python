from datetime import datetime

#área das funções
#função que apresenta a msg de bom dia, boa tarde ou boa noite
def saudacoes():

    agora = datetime.now()


    hora = agora.hour

    if (hora >= 6 and hora <= 12):
        print("Olá, Bom Dia!!!")
    elif (hora > 12 and hora <= 13):
        print("Olá, Boa Tarde!!!")
    else:
        print("Olá, Boa Noite!!!")

#Esta recebe um parametro do tipo string
def saudacoes2(param1:str):
    agora = datetime.now()
    hora = agora.hour

    if (hora >= 6 and hora <= 12):
        print(f"Olá {param1}, Bom Dia!!!")
    elif (hora > 12 and hora <= 13):
        print(f"Olá {param1}, Boa Tarde!!!")
    else:
        print(f"Olá {param1}, Boa Noite!!!")

#Função que devolve o maior entre dois números 
def maior(n1:int, n2:int) -> int: #-> int devolve o valor em int
    
    #faz a devolução da info compatível com o tipo informado
    if n1 > n2:
        return n1 #return encerra a função e retorna o valor em n1
    else:
        return n2

nome = input("Qual seu nome? ")

#saudacoes()
saudacoes2(nome)
saudacoes2 ("Carlos Eduardo")

print("Mostra o maior entre dois números")
maior(10, 70) #não faz nada com o valor devolvido

#jogando o valor para a variavel
res = maior(23, 76)
print(f"O maior número é {res}")
#ou puxar a função direto
print(f"Outra forma de achar o maior: {maior(23, 76)}")