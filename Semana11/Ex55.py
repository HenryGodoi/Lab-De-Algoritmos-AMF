
valores = []
maior100 = []
contar = 0

for i in range(10):
    valor = int(input("Digite: "))
    valores.append(valor)

for i in range(len(valores)):
    if valores[i] > 100:
        contar += 1
        maior100.append(valores[i])

print(f"{contar} valores são maiores que 100")
print(f"Sendo eles: {maior100}")
