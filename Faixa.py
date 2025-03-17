#indica a faixa de acordo com o valor dado
valor = 0.0

valor = float(input("Insira um valor: "))

if (0 <= valor <= 10):
  print("O valor dado pertence a faixa 1")
elif (15 <= valor <= 25):
  print("O valor dado pertence a faixa 2")
elif (26 <= valor <= 40):
  print("O valor dado pertence a faixa 3")
else:
  print("O valor não possui faixa definida")