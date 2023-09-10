print(5*"*", " Ordenar los numeros ", 5*"*")

numeros = []

for i in range(0, 4):
    numero = int(input("ingrese un numero: "))
    numeros.append(numero)

for i in range(0, len(numeros)-1):
    for j in range(0, len(numeros)-1):
        if numeros[j] > numeros[j+1]:
            aux = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = aux

print(numeros)