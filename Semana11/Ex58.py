
itens = []
item = 0
opc = 0
retirar = 0

while opc != 5:
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens (um elemento por linha)")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    opc = int(input("Opção: "))

    if opc == 1:
        item = int(input("Insira o item: "))
        itens.append(item)
    elif opc == 2:
        retirar = int(input("Retirar item na posição: "))
        itens.remove(retirar)
    elif opc == 3:
        for i in range(len(itens)):
            print(itens[i])
    elif opc == 4:
        itens.clear()
        print("Todos os itens foram retirados.")
    elif opc == 5:
        print("Saindo...")
    else:
        print("Erro, tente uma opção que existe.")
