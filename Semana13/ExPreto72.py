 
def ler_safra():
    safra = []
 
    for i in range(5):
        valor = int(input(f"Digite a quantidade colhida (kg) na colheita {i+1}: "))
        safra.append(valor)
 
    return safra
 
def calcular_soma(safra):
    soma = 0
 
    for i in range(len(safra)):
        soma += safra[i]
 
    return soma
 
def calcular_media(soma):
    media = soma / 5
    return media
 
def exibir_soma_media(safra):
    soma = calcular_soma(safra)
    media = calcular_media(soma)
 
    print(f"\nSoma total da safra: {soma} kg")
    print(f"Média por colheita: {media:.2f} kg")
 
def main():
    safra = ler_safra()
    exibir_soma_media(safra)
 
main()
