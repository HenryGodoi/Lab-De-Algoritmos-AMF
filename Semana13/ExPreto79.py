 
def ler_kg_colhidos():
    kg = []
 
    for i in range(5):
        valor = float(input(f"Digite os kg colhidos da árvore {i+1}: "))
        kg.append(valor)
 
    return kg
 
def ler_precos():
    precos = []
 
    for i in range(5):
        valor = float(input(f"Digite o preço por kg da árvore {i+1} (R$): "))
        precos.append(valor)
 
    return precos
 
def calcular_valor_por_arvore(kg, precos):
    valores = []
 
    for i in range(len(kg)):
        valor = kg[i] * precos[i]
        valores.append(valor)
 
    print("\n--- Valor obtido por árvore ---")
    for i in range(len(valores)):
        print(f"Árvore {i+1}: {kg[i]} kg × R${precos[i]:.2f} = R${valores[i]:.2f}")
 
    return valores
 
def main():
    print("\n[ Produção (kg) ]")
    kg = ler_kg_colhidos()
 
    print("\n[ Preço por kg ]")
    precos = ler_precos()
 
    calcular_valor_por_arvore(kg, precos)
 
main()
