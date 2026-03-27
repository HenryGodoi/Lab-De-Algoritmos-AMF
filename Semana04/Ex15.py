
valor_compra = float(input("valor da compra: "))
print("1 - Pagamento à vista (4 porcentos de desconto)") 
print("2 - Em 12x (2 porcento de juros)")
print("3 - Em 24x (7 porcento de juros)")
print("4 - Em 36x (15 porcento de juros)")

opçao = int(input("Digite a opção: "))
if opçao == 1:
    valor_final = valor_compra * 0.96
    print("Valor com desconto:",  valor_final)
elif opçao == 2:
    valor_final = valor_compra * 1.02
    parcela = valor_final / 12
    print("Valor com juros:", valor_final, "valor da parcela:", parcela)
elif opçao == 3:
    valor_final = valor_compra * 1.07
    parcela = valor_final / 24
    print("Valor com juros:", valor_final, "valor da parcela:", parcela)
elif opçao == 4:
    valor_final = valor_compra * 1.15
    parcela = valor_final / 36
    print("Valor com juros:", valor_final, "valor da parcela:", parcela)
else:
    print("Opção inválida.")
