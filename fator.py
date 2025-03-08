def mult(a, b):
  return a * b

parametro = 4
resultado = 1

for i in range(1, parametro + 1):
  if(parametro == 1):
    print ("ta de brincadera, muito facil")
  else:
    resultado = mult(resultado, i)

print (resultado)