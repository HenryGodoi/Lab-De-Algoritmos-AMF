
def somaImposto(taxaImposto, valor):    
    valorFinal = valor * taxaImposto
    print(valorFinal)

def main():
    valor = int(input("Digite o valor: "))
    imposto = int(input("Digite o imposto: "))
    somaImposto(imposto, valor)

main()
