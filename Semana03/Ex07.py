
horas_trabalhadas = float(input("Digite o total de horas trabalhadas no mês: "))
salario = 35.00
salario_final = salario * horas_trabalhadas

if salario_final < 1000.00:
    salario_final += 300.00
    print ("O salário final do funcionário será: R$", salario_final)
else:
    print ("O salário final do funcionário será: R$", salario_final)
