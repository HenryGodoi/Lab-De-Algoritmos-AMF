
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    desconto = valor_compra * 10 / 100
    valor_final = valor_compra - desconto
    print("O valor final da compra com desconto é: R$", valor_final)
else:
    print("O valor final da compra é: R$", valor_compra)
