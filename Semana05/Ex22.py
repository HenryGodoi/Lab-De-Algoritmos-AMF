
nome = input("Digite o nome: ")
salario = float(input("Digite o sálario: "))
tempo = float(input("Tem de serviço na equipe(em anos): "))

if tempo >= 5 and salario <= 2000:
    salariof = salario + (salario * 0.1)
    salarioau = salariof - salario
    print(f"{nome} o seu salário teve um aumento de {salarioau}, logo o seu novo salário se torna {salariof}, Parabéns!")
else:
    salariof = salario + (salario * 0.05)
    salarioau = salariof - salario
    print(f"{nome} o seu salário teve um aumento de {salarioau}, logo o seu novo salário se torna {salariof}, Parabéns!")
