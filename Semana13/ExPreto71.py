
def ler_colheitas():
    colheitas = []
 
    for i in range(5):
        valor = int(input(f"Digite a produção (kg) da colheita {i+1}: "))
        colheitas.append(valor)
 
    return colheitas
 
def inverter_colheitas(colheitas):
    invertido = []
 
    for i in range(len(colheitas) - 1, -1, -1):
        invertido.append(colheitas[i])
 
    print(f"\nColheitas em ordem inversa: {invertido}")
 
    return invertido
 
def main():
    colheitas = ler_colheitas()
    inverter_colheitas(colheitas)

main()
