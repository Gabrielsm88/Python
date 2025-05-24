#Criando matriz 4x3
matriz = [[0 for coluna in range(4)] for linha in range(3)]  #mais fácil para matrizes muito grandes
#ou
matriz = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

#gerando a sequencia dos indices para entrada de dados
for linha in range(3):
    for coluna in range(4):
        matriz[linha[coluna]] = int(input(f"Matriz[{linha}]"))

#varredura na matriz, para exibir seu conteudo
for linha in range(3):

    for coluna in range(4):
        print(f"{matriz[linha][coluna]} \t", end='')  #

    print("") #pular linha
