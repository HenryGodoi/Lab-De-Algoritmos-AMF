
opc = 0
opc1 = 0
opc2 = 0
opc3 = 0

for jornal in range(1, 21):
    print("1° opção - Jornal A")
    print("2° opção - Jornal B")
    print("3° opção - Jornal C")
    opc = int(input("Digite a sua opção(1, 2 ou 3): "))
    
    if opc == 1:
        opc1 += 1
    elif opc == 2:
        opc2 += 1
    elif opc == 3:
        opc3 += 1
    else:
        print("Erro, escolha uma das opções(1°, 2° ou 3°).")
    
porcentagem1 = [(opc1 * 100) / 20]
porcentagem2 = [(opc2 * 100) / 20]
porcentagem3 = [(opc3 * 100) / 20]

if porcentagem1 > porcentagem2 > porcentagem3:
    print(f"O jornal em 1° Lugar ficou o Jornal A com {porcentagem1}%, ficando em 2° lugar o Jornal B com {porcentagem2} e em último lugar o Jornal C com {porcentagem3}")
elif porcentagem1 > porcentagem3 > porcentagem2:
    print(f"O jornal em 1° Lugar ficou o Jornal A com {porcentagem1}%, ficando em 2° lugar o Jornal C com {porcentagem3} e em último lugar o Jornal B com {porcentagem2}")
elif porcentagem2 > porcentagem1 > porcentagem3:
    print(f"O jornal em 1° Lugar ficou o Jornal B com {porcentagem2}%, ficando em 2° lugar o Jornal A com {porcentagem1} e em último lugar o Jornal C com {porcentagem3}")
elif porcentagem2 > porcentagem3 > porcentagem1:
    print(f"O jornal em 1° Lugar ficou o Jornal B com {porcentagem2}%, ficando em 2° lugar o Jornal C com {porcentagem3} e em último lugar o Jornal A com {porcentagem1}")
elif porcentagem3 > porcentagem1 > porcentagem3:
    print(f"O jornal em 1° Lugar ficou o Jornal C com {porcentagem3}%, ficando em 2° lugar o Jornal A com {porcentagem1} e em último lugar o Jornal B com {porcentagem2}")
elif porcentagem3 > porcentagem2 > porcentagem1:
    print(f"O jornal em 1° Lugar ficou o Jornal C com {porcentagem3}%, ficando em 2° lugar o Jornal B com {porcentagem2} e em último lugar o Jornal A com {porcentagem1}")
