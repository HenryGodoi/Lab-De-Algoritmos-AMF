
numeros = 0
soma_numeros = 0

for numero in range(1, 11):
    numeros = int(input("Digite os números: "))
    soma_numeros += numeros

media = soma_numeros / 10

print("A média aritmética é: ", media)
