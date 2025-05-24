#VARIAVEIS
cateto1 = 0.0
cateto2 = 0.0
area = 0.0
hipotenusa = 0.0

#INPUT
cateto1 = float(input("Digite o valor do cateto: "))
cateto2 = float(input("Digite o valor do outro cateto: "))

#CÁLCULOS
import math
hipotenusa = math.sqrt((cateto1*cateto1)+(cateto2*cateto2))
area = cateto1*cateto2/2

#OUTPUT
print(f"A hipotenusa é: {hipotenusa}")
print(f"A área é: {area}")
