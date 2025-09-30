# Gabriel de Souza Magalhães
# Matheus Feliciano das Neves

# -------- Programa principal -------- #
N = int(input().strip())  
canais = ler_canais(N)  # Lê todos os canais recursivamente
X, Y = map(float, input().strip().split()) 

print("-----")
print("BÔNUS")
print("-----")

resultados = processar_canais(canais, X, Y)  # Calcula bônus de todos
imprimir_resultado(resultados)  # Imprime recursivamente


# -------- Funções -------- #
def ler_canais(n):
    # Lê os dados dos canais recursivamente.
    if n == 0:  # Se não houver canais para ler
        return []
    entrada = input().strip().split(";") # Lê e separa os dados pelo ";"
    nome = entrada[0]
    inscritos = int(entrada[1])
    monetizacao = float(entrada[2])
    premium = entrada[3].lower() == "sim"
    # Retorna o canal atual + chamada recursiva para os próximos
    return [(nome, inscritos, monetizacao, premium)] + ler_canais(n - 1)


def calcular_bonus(canal, X, Y):
    # Calcula o bônus de um único canal.
    nome, inscritos, monetizacao, premium = canal
    bonus = monetizacao + (inscritos * X)  
    if premium:  # Se for premium, adiciona Y
        bonus += Y
    return (nome, bonus)


def processar_canais(canais, X, Y):
    # Processa os canais recursivamente, retornando lista de bônus
    if not canais:  # Se for uma lista vazia
        return []
    canal_atual = canais[0]  # Pega o primeiro canal
    nome, bonus = calcular_bonus(canal_atual, X, Y)  # Calcula bônus
    # Retorna canal processado + recursão para o resto da lista
    return [(nome, bonus)] + processar_canais(canais[1:], X, Y)


def imprimir_resultado(canais):
    # Imprime os resultados recursivamente
    if not canais:  
        return
    nome, bonus = canais[0]  
    print(f"{nome}: R$ {bonus:.2f}")  # Imprime o bônus
    imprimir_resultado(canais[1:])  # Chama recursivamente para o resto