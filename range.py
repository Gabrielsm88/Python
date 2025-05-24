#indica a faixa de acordo com o valor dado
valor = 0.0

valor = float(input("Insira um valor: "))

if (valor >= 0 and valor <= 10):
  print("O valor dado pertence a faixa 1")
elif (valor >= 15 and valor <= 25):
  print("O valor dado pertence a faixa 2")
elif (valor >= 26 and valor <= 40):
  print("O valor dado pertence a faixa 3")
else:
  print("O valor não possui faixa definida")
