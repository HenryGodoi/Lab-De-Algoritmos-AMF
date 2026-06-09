
def ler_lotes():
    lotes = []
 
    for i in range(10):
        valor = int(input(f"Digite o código do lote {i+1}: "))
        lotes.append(valor)
 
    return lotes
 
def inverter_lotes(lotes):
    invertido = []
 
    for i in range(len(lotes) - 1, -1, -1):
        invertido.append(lotes[i])
 
    print(f"\nLotes em ordem inversa: {invertido}")
 
    return invertido
 
def main():
    lotes = ler_lotes()
    inverter_lotes(lotes)

main()
