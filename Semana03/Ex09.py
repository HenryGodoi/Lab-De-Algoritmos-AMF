
idade = int(input("Digite o seu ano de nascimento: "))
anoatual = 2026
idadevotar = anoatual - idade

if idadevotar >= 16:
    print("Você pode votar.")
    if idadevotar > 70:
        print("Você não é mais obrigado a votar.")
else:
    print("Você não pode votar.")
