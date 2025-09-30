noiva = set()
noivo = set()

while True:
    entrada = input().strip()
    if entrada == "ACABOU":
        break
    X, Y = entrada.split(";") # X(nome), Y(noivos)
    if Y == "noiva":
        noiva.add(X)
    elif Y == "noivo":
        noivo.add(X)

# a - lista final
a = sorted(noivo | noiva)

# b - lista da noiva
b = sorted(noiva - noivo)

# c - lista do noivo
c = sorted(noivo - noiva)

# d - lista em comum
d = sorted(noivo & noiva)

# e - lista de apenas um
e = sorted(noivo ^ noiva)

# Nome das Listas
listas = [
    ("LISTA FINAL", a),
    ("APENAS NOIVA", b),
    ("APENAS NOIVO", c),
    ("POR AMBOS", d),
    ("POR APENAS UM DELES", e)
]

for i,(titulo, convidados) in enumerate(listas):
    print("-" * 20)
    print(titulo)
    print("-" * 20)
    for X in convidados:
        print(X)
    if i < len(listas) - 1: # Verifica se tem mais titulos
        print("*")