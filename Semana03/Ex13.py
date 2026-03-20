
h = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu genero (M para masculino ou F para feminino): ").upper()

if sexo == 'M':
    peso_ideal = (72.7 * h) - 58
    print("O peso ideal para um homem com altura", h, "m é:", peso_ideal, "kg")
elif sexo == 'F':
    peso_ideal = (62.1 * h) - 44.7
    print("O peso ideal para uma mulher com altura", h, "m é:", peso_ideal, "kg")
else:
    print("Letra inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")
