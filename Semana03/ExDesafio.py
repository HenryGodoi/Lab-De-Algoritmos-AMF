
nomecliente = input("Digite o nome do cliente: ")
valororiginal = float(input("Digite o valor da compra: "))
Formadepgmto = input("Digite a forma de pagamento (1 - Dinheiro, 2 - Cartão): ")
print("")

print ("--Informações da compra--")
print ("O nome do cliente é:", nomecliente)
if valororiginal > 200:
    if Formadepgmto == "1":
            valorfinal = valororiginal - (valororiginal * 15 / 100)
            print("O valor original da compra é: R$", valororiginal)
            print("O valor final da compra com desconto é: R$", valorfinal)
    elif Formadepgmto == "2":
            valorfinal = valororiginal - (valororiginal * 5 / 100)
            print("O valor original da compra é: R$", valororiginal)
            print("O valor final da compra com desconto é: R$", valorfinal)
        
if valororiginal <= 200:
    if Formadepgmto == "1":
        valorfinal = valororiginal - (valororiginal * 10 / 100)
        print("O valor original da compra é: R$", valororiginal)
        print("O valor final da compra com desconto é: R$", valorfinal)
    elif Formadepgmto == "2":
        valorfinal = valororiginal
        print("O valor original da compra é: R$", valororiginal)
        print("A compra não irá receber desconto, valor final: R$", valorfinal)
