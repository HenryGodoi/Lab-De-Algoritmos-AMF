
def menu():
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostar saldo")
    print("4 - Sair")
    opc = int(input("Opção: "))
    return opc

def mostrar_saldo(saldo):
    print("Saldo atual:", saldo)

def sacar(saldo):
    valor = float(input("Valor para saque: "))
    if valor <= saldo:
        saldo -= valor
        mostrar_saldo(saldo)
    else:
        print("Saldo insuficiente.")
    return saldo

def depositar(saldo):
    valor = float(input("Valor para deposito: "))
    saldo += valor
    mostrar_saldo(saldo)
    return saldo

def main():
    saldo = 0
    opc = 0

    while opc != 4:
        opc = menu()
        if opc == 1:
            saldo = sacar(saldo)
        elif opc == 2:
            saldo = depositar(saldo)
        elif opc == 3:
            mostrar_saldo(saldo)
        elif opc == 4:
            print("Saindo..")

main()
