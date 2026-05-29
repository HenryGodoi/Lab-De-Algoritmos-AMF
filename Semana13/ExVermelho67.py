
def valores():
    azeitonas = []
    soma = 0
    
    for i in range(8):
        valor = int(input(f"Digite o valor {i+1}°: "))
        azeitonas.append(valor)
    
    for i in range(8):
        soma += azeitonas[i]
        
    return soma

def media(azeitona):
    calculo = azeitona / 8
    print(f"A média é: {calculo}")
    
    return calculo


def main():
    azeitona = valores()

    media(azeitona)

main()
