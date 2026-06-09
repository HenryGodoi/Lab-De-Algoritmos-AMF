 
def ler_lotes_extracao():
    lotes = []
 
    for i in range(6):
        valor = float(input(f"Digite os kg de azeitona do lote {i+1}: "))
        lotes.append(valor)
 
    return lotes
 
def ler_rendimento():
    rendimento = float(input("Digite o rendimento de extração (ex: 0.18 para 18%): "))
    return rendimento
 
def calcular_litros(lotes, rendimento):
    litros = []
 
    for i in range(len(lotes)):
        resultado = lotes[i] * rendimento
        litros.append(resultado)
 
    print(f"\nRendimento aplicado: {rendimento * 100:.0f}%")
    for i in range(len(litros)):
        print(f"Lote {i+1}: {lotes[i]} kg → {litros[i]:.2f} litros de azeite")
 
    return litros
 
def main():
    lotes = ler_lotes_extracao()
    rendimento = ler_rendimento()
    calcular_litros(lotes, rendimento)
 
main()
