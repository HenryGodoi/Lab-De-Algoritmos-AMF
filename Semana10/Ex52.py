
dentro = 0
fora = 0

for intervalo in range(1, 11):
    numero = float(input(f"Digite o {intervalo}° número: "))

    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1

print(f"Estão dentro do intervalo, {dentro} números")
print(f"Está fora do intervalo, {fora} números")
