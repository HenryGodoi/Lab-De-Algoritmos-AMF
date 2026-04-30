
valor_combustivel = float(input())

distri_revenda = valor_combustivel * 0,17
custo_etanol = valor_combustivel * 0,12
icms = valor_combustivel * 0,28
#c_pis/pasep_cofins = valor_combustivel * 0,07 (Código errado)
c_pis_pasep_cofins = valor_combustivel * 0,07 #notei que a variavel tinha um / entre o pis e o pasep e por isso o código não funcionou corretamente por conta desse erro

diminuir = distri_revenda + custo_etanol + icms + c_pis_pasep_cofins

valor_refinaria = valor_combustivel - diminuir

print(valor_combustivel)
print(distri_revenda)
print(custo_etanol)
print(icms)
print(c_pis_pasep_cofins)
print(valor_refinaria)
