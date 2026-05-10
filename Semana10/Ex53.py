# Uma empresa de pesquisa deseja saber qual jornal é mais lido em Santa Maria (A, B ou C). 
# Faça um algoritmo que leia a opinião de 20 pessoas, ao final mostre a porcentagem de cada uma das revistas, em ordem crescente.

opc = 0
opc1 = 0
opc2 = 0
opc3 = 0

for jornal in range(1, 21):
    print("1° opção - Jornal A")
    print("2° opção - Jornal B")
    print("3° opção - Jornal C")
    opc = int(input("Digite a sua opção: "))
    
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
