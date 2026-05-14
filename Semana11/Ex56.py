
valores = []
pares = []

for i in range(10):
    valor = int(input("Digite: "))
    valores.append(valor)

pos_pares = 0
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
        print(f"{i}°: {pares[pos_pares]}")
        pos_pares += 1 
