
ingressos = 100
opcao = 0

while opcao != 4:
    print("1 - Diminuir quantidade de ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        diminuir = int(input("Digite a quantidade de ingressos para diminuir: "))
        ingressos -= diminuir
    elif opcao == 2:
        adicionar = int(input("Digite a quantidade que você deseja adicionar: "))
        ingressos += adicionar
    elif opcao == 3:
        print(f"Atualmente está disponivel {ingressos} para compra.")
    elif opcao == 4:
        print("Finalizando...")
    else:
        print("Opção Inválida.")
    
