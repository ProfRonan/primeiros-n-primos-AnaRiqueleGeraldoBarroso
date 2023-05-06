num = int(input("Digite um número: "))
cont = 0
n = 2 
while cont < num:
    primo = True
    for i in range(2, n):
        if n % i == 0:
           primo = False
           break
    if primo:
        print(n)
        cont += 1
    n += 1