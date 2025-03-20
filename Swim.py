#indica a categoria do nadador de acordo com a idade dele
idade = 0

idade = int(input("Qual a idade do nadador? "))

if idade < 5 :
  print("Sem categoria")
elif (idade <= 7):
  print("Infantil A")
elif (idade<= 10):
  print("Infantil B")
elif (idade <= 13):
  print("Juvenil A")
elif (idade <= 17):
  print("Juvenil B")
elif (idade <= 60):
  print("Adulto")
else:
  print("Senior")
  