
print("Opções de kit:")
print("1 - Kit Básico: Número de peito + medalha = R$100,00")
print("2 - Kit Plus: Número de peito + medalha + camiseta = R$120,00")
print("3 - Kit Premium: Número de peito + medalha + camiseta + squeeze + boné = R$150,00")

opcao = int(input("\nDigite a opção escolhida: "))
valor_entregue = float(input("Digite o valor entregue em R$: "))

if opcao == 1:
    valor_kit = 100.00
    categoria = "Kit Básico"
elif opcao == 2:
    valor_kit = 120.00
    categoria = "Kit Plus"
elif opcao == 3:
    valor_kit = 150.00
    categoria = "Kit Premium"
else:
    print("Opção inválida.")

if valor_entregue >= valor_kit:
    troco = valor_entregue - valor_kit
    print(f"\nO valor foi suficiente. A sua categoria de atleta: {categoria}. O seu troco: R$ {troco:.2f}")
else:
    print("O valor foi insuficiente.")
