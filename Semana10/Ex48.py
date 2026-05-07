
numero = 0
numeros_pares = 0
numeros_impares = 0
numeros_zeros = 0

for i in range(0, 11):
    numero = int(input("Digite o seu número: "))

    if numero == 0:
        numeros_zeros += 1
    elif numero % 2 == 0:
        numeros_pares += 1
    elif numero % 2 == 1:
        numeros_impares += 1
    
print(numeros_pares)
print(numeros_impares)
print(numeros_zeros)
