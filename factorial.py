# Calculo do fatorial de um número fornecido pelo usuario

fatorial = 1
num = int(input("Digite o fatorial que quer calcular: "))

print(f"{num}! = ", end = '')

#laço de repetição
for n in range(num, 0, -1):
    fatorial = fatorial * n
    if n > 1:
     print(f"{n} x ", end = '')
    else:
        print(f"{n} = {fatorial}")
