
litro = float(input("Digite quantos litros você colocou: "))
valor = float(input("Digite o valor da gasolina: "))

valort = litro * valor

if litro >= 20 and valort > 100:
    desconto = valort - (valort * 0.10)
    print(f"Você obteve um desconto de 10 porcentos, logo o valor final ficará: {desconto}")
elif litro >= 20 and valort <= 100:
    desconto = valort - (valort * 0.05)
    print(f"Você obteve um desconto de 5 porcentos, logo o valor final ficará: {desconto}")
else:
    print(f"O valor final do seu abastecimento será: {valort}")
