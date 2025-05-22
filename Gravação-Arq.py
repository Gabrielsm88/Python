#incompleto!!! (terminar o import para arquivo)
import os.path


if not os.path.exists("Ranking.txt"):
    print("O arquivo Ranking.txt, não existe")

#aBRE O ARQ NO MODO ESCRITA
# r -> LEITURA
# w -> GRAVAÇÃO, SE JÁ EXISTIR APAGA E CRIA
# a -> append, se existir, preserva o conteúdo e adiciona ao final 
rank = open("Ranking.txt", "a")

#faz a leitura do arquivo todo e o coloca dentro de uma lista
for linha in rank.readlines():
    #função strip() remove o enter ou \n da variavle
    #print(f"conteudo: {linha.strip()}")

    #desmembrando a string
    #retira o \n e depois desmembra
    parte = linha.strip().split("#")

    #print dados
    print(f"Nome: {parte[0]}")
    print(f"Data: {parte[1]}")
    print(f"Nível: {parte[2]}")
    print(f"Resultado: {parte[3]}")
    print("-----------------------------------------------")

print("Fim de arquivo")


#Variaveis
nome = ""
data = ""
nivel = ""
resultado = ""

#main
while(True):
    nome = input("Nome do jogador: ")
    data = input("Data da partida: ")
    nivel - input("Nívek de dificuldade: ")
    resultado = input("Resultado da partida: ")

    #montar a linha para ser gravada é colocolado \n para pular a linha
    linha = f"{nome}#{data}#{nivel}#{resultado}\n"

    #faz a gravação
    rank.write(linha)

    #outro jogador
    resp = input("Gravar outro jogador (S/N): ").UPPER()

    if(resp != "S"):
        break

#fecha o arquivo
rank = exit("Ranking.txt", "a")