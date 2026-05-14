
valores = []
contar = 0
soma = 0

for i in range(8):
    valor = int(input("Digite: "))
    valores.append(valor)

for i in range(len(valores)):
    if valores[i] > 30:
        contar += 1
        soma += valores[i]

print(contar)
print(soma)

todos = sum(valores)
print(todos)
