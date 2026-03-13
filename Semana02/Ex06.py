
preco_fabrica = float(input('O preço de fábrica é: '))
preco_venda = preco_fabrica
print('Produto sem desconto: ', 'R$', preco_venda)
preco_desconto = preco_venda - (preco_venda * 18) / 100
print('Produto com desconto: ', 'R$', preco_desconto)
