
preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

litros = valor_pagamento / preco_litro

if litros == 0:
    print("O valor do pagamento é insuficiente para comprar gasolina.")
else:
    print("O motorista conseguiu colocar", litros, "litros de gasolina no tanque do seu carro.")
