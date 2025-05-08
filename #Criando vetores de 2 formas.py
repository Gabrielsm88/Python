#Criando vetores de 2 formas 
idade = [0, 0, 0, 0, 0]
#ou
idade = (0 for aux in range(6))

#IN
for ind in range(len(idade)):
    idade[int] = int(input(f"Digite a {ind + 1}ª idade: "))

#Listar as idades sem saber o indice
for dado in idade:
    print(f"Idade -. {dado}")
    
#Listar as idades sabendo o indice
for ind in range(len(idade)):
    print(f"Idade = {idade[ind]}")