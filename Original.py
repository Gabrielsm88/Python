#Ler vetor Original e apresentar no vetor destino sua multiplicação por 3
#94
Original = Destino = [0, 0, 0, 0, 0, 0, 0]  #Criando vetores

for i in range(7):  #repetição de entrada de dados e multiplicação
    Original = int(input("Digite um número: "))
    Destino[i] = [Original*3]

for i in range(7): #print destino
    print(f"Destino = {Destino[i]}")
    