
def exibir_menu():
    print("------------------------")
    print(" GERENCIAMENTO DE LOTES")
    print("------------------------")
    print("1. Inserir lote")
    print("2. Listar lotes")
    print("3. Retirar um lote")
    print("4. Limpar todos os lotes")
    print("5. Contar lotes com código/produção maior que X")
    print("6. Verificar se um código está presente")
    print("7. Encontrar maior e menor código")
    print("8. Sair")
    
    return int(input("Escolha uma opção: "))

def inserir_lote(lotes):
    codigo = int(input("Digite o código do lote (apenas números pares): "))
    
    if codigo % 2 == 0:
        lotes.append(codigo)
        print(f"Sucesso! Lote {codigo} inserido.")
    else:
        print("Erro: O código digitado é ímpar. Apenas valores pares são aceitos.")


def listar_lotes(lotes):
    if len(lotes) == 0:
        print("O array de lotes está vazio no momento.")
    else:
        print(f"Lotes registrados: {lotes}")


def retirar_lote(lotes):
    codigo = int(input("Digite o código do lote que deseja retirar: "))
    
    if codigo in lotes:
        lotes.remove(codigo)
        print(f"Lote {codigo} removido com sucesso!")
    else:
        print("Erro: Este código de lote não foi encontrado no array.")


def limpar_lotes(lotes):
    lotes.clear()
    print("Todos os lotes foram limpos com sucesso!")


def contar_maiores_que_x(lotes):
    if len(lotes) == 0:
        print("O array está vazio.")
        return
        
    x = int(input("Digite o valor de X: "))
    contador = 0
    
    for i in range(len(lotes)):
        if lotes[i] > x:
            contador += 1
            
    print(f"Temos {contador} lote(s) com valor maior que {x}.")


def verificar_presenca(lotes):
    codigo = int(input("Digite o código que deseja procurar: "))
    
    for i in range(len(lotes)):
        if lotes[i] == codigo:
            print(f"O código {codigo} ESTÁ presente no sistema.")
            return 
            
    print(f"O código {codigo} NÃO está presente.")


def encontrar_maior_menor(lotes):
    if len(lotes) == 0:
        print("O array está vazio, não há maior nem menor.")
        return
        
    maior = lotes[0]
    menor = lotes[0]
    
    for i in range(len(lotes)):
        if lotes[i] > maior:
            maior = lotes[i]
        if lotes[i] < menor:
            menor = lotes[i]
            
    print(f"O MAIOR código registrado é: {maior}")
    print(f"O MENOR código registrado é: {menor}")


def main():
    array_lotes = []
    opcao = 0
    
    while opcao != 8:
        opcao = exibir_menu()
        
        if opcao == 1:
            inserir_lote(array_lotes)
        elif opcao == 2:
            listar_lotes(array_lotes)
        elif opcao == 3:
            retirar_lote(array_lotes)
        elif opcao == 4:
            limpar_lotes(array_lotes)
        elif opcao == 5:
            contar_maiores_que_x(array_lotes)
        elif opcao == 6:
            verificar_presenca(array_lotes)
        elif opcao == 7:
            encontrar_maior_menor(array_lotes)
        elif opcao == 8:
            print("Encerrando o programa...")
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 8.")

main()
