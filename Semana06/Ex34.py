
opc = 0
valorv = 0
retirardin = 0
caixa = 0

print("Qual o dinheiro no caixa atual?")
while opc != 4:
    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")
    opc = int(input("Digite a sua opção: "))
    
    if opc == 1:
        valorv = int(input("Digite o valor da venda: "))
        caixa += valorv
    elif opc == 2:
        retirardin = int(input("Digite o valor que deseja retirar do caixa: "))
        caixa -= retirardin
    elif opc == 3:
        print(f"O valor atual do caixa é: R$ {caixa}.")
    elif opc == 4:
        print("Saindo...")
    else:
        print("Opção inválida.") 
