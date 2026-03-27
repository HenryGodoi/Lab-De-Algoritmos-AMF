
ingresso = float(input("Digite o valor do ingresso: "))
print("Opções:")
print("1 - Ingresso normal")
print("2 - Estudante (50 porcento de desconto)")
print("3 - Criança até 12 anos (40 porcento de desconto)")
print("4 - Idoso (60 porcento de desconto)")
opcao = int(input("Digite a opção escolhida: "))

if opcao == 1:
    valor_final = ingresso
    print("O valor a ser pago é: R$", valor_final)
elif opcao == 2:
    valor_final = ingresso * 0.50
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")
elif opcao == 3:
    valor_final = ingresso * 0.40
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")
elif opcao == 4:
    valor_final = ingresso * 0.60
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")
else:
    print("Opção inválida.")
