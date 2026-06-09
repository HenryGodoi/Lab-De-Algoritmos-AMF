 
def ler_producoes():
    producoes = []
 
    for i in range(5):
        valor = int(input(f"Digite a produção (kg) da árvore {i+1}: "))
        producoes.append(valor)
 
    return producoes
 
def encontrar_maior_menor(producoes):
    maior = producoes[0]
    menor = producoes[0]
    pos_maior = 0
    pos_menor = 0
 
    for i in range(len(producoes)):
        if producoes[i] > maior:
            maior = producoes[i]
            pos_maior = i
        if producoes[i] < menor:
            menor = producoes[i]
            pos_menor = i
 
    print(f"\nMaior produção: {maior} kg — Árvore {pos_maior + 1} (índice {pos_maior})")
    print(f"Menor produção: {menor} kg — Árvore {pos_menor + 1} (índice {pos_menor})")
 
def main():
    producoes = ler_producoes()
    encontrar_maior_menor(producoes)
 
main()
