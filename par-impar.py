def parouimp(n):
    if n == 0:
        return True
    else:
            if n == 1:
                return False
            else:
                return parouimp(n - 2)
               
n = int(input())

if parouimp(n):
    print("numero par")
else:
    print("numero nao par")