
inscrição = float(input("Valor da Inscrição: "))
print("1 - Pagamento à vista") 
print("2 - Em 2x")
print("3 - Em 3x")

opçao = int(input("Digite a opção: "))

if opçao == 1:
    print("O valor a ser pago será:", inscrição)
elif opçao == 2:
    parcela = inscrição / 2
    print(f"O valor de cada parcela será: {parcela:.2f}")
elif opçao == 3:
    parcela = inscrição / 3
    print(f"O valor de cada parcela será: {parcela:.2f}")
else:
    print("Opção inválida.")
