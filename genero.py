def valida(dado: str) -> bool:
    if dado[0].upper() == "M" or dado[0].upper() == "F":    
    #if dado[0].upper() in "MF"
        return True
    else:
        return False
        
sexo = input("Digite o seu sexo (M/F): ")
while not valida(sexo):
    print("Informação inválida, tente outra vez!!!")
    sexo = input("Digite o seu sexo (M/F): ")