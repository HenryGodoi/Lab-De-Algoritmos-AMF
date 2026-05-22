
def receber_valor():
    valor = int(input("Digite: "))
    return valor

def calculos(valor):
    dobro = valor * 2
    print(dobro)
    triplo = valor * 3
    print(triplo)

def main():
    valor = receber_valor()
    calculos(valor)

main()
