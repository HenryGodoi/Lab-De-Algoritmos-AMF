
def valor_total():
    comprar = int(input("Quantidade: "))
    return comprar

def calculo(comprar):
    if comprar <= 12:
        laranjas = 0.40 * comprar
    elif comprar > 12:
        laranjas = 0.25 * comprar
    print("Valor final:", laranjas)


def main():
    total = valor_total()
    calculo(total)

main()
