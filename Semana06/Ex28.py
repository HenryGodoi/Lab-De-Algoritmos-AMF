
code_brinquedo = 1
carrinho_CR = 1040
contador = 0

while code_brinquedo != 0:
    code_brinquedo = int(input("Digite o código: "))

    if code_brinquedo == carrinho_CR:
        contador += 1
        print("O seguinte código é do carrinho de controle remoto.")
        print("A quantidade de vezes que o código foi  selecionado: ", contador)
    elif code_brinquedo != carrinho_CR:
        print("Esse código não pertence a nenhum brinquedo.")
    elif code_brinquedo == 0:
        print('Saindo...')
