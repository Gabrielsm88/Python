#indica a categoria do nadador de acordo com a idade dele
idade = 0

idade = int(input("Qual a idade do nadador? "))

if idade < 5 :
  print("Sem categoria")
elif (5 <= idade <= 7):
  print("Infantil A")
elif (8 <= idade <= 10):
  print("Infantil B")
elif (11 <= idade <= 13):
  print("Juvenil A")
elif (14 <= idade <= 17):
  print("Juvenil B")
elif (18 <= idade <= 60):
  print("Adulto")
else:
  print("Senior")
  