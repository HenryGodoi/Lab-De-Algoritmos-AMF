
dias = 0
oliveiras = 0
total_oliveiras = 0
dia_maior = 0
dia_menor = 0
oliveira_maior = 0
oliveira_menor = 0

oliveiras = int(input("Digite a quantidade de oliveiras colhidas: "))
total_oliveiras += oliveiras
oliveira_maior = oliveira_menor = oliveiras
dias += 1

while dias < 7:
    oliveiras = int(input("Digite a quantidade de oliveiras colhidas: "))
    total_oliveiras += oliveiras

    if oliveira_maior < oliveiras:
        oliveira_maior = oliveiras
        dia_maior = dias
    elif oliveira_menor > oliveiras:
        oliveira_menor = oliveiras
        dia_menor = dias

    dias += 1
dia_menor += 1
dia_maior += 1

print(f"\nO total de oliveiras colhidas na semana foi: {total_oliveiras} oliveiras.")
print(f"O dia com maior colheita foi o {dia_maior}° dia.")
print(f"O dia com menor colheita foi o {dia_menor}° dia.")
