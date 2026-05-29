
def fazendaA():
    producao = []
    numero = int(input("Quantos lotes?"))

    for i in range(numero):
        valor = int(input(f"Digite a produção (kg) do lote {i+1} da Fazenda A: "))
        producao.append(valor)
        
    return producao

def fazendaB():
    producao = []
    numero = int(input("Quantos lotes?"))

    for i in range(numero):
        valor = int(input(f"Digite a produção (kg) do lote {i+1} da Fazenda B: "))
        producao.append(valor)
        
    return producao

def soma_producao(prod_a, prod_b):
    producao_total = []
    
    for i in range(len(prod_a)):
        soma = prod_a[i] + prod_b[i]
        producao_total.append(soma)
        
    print(f"\nA produção total por lote (Fazenda A + Fazenda B) é: {producao_total}")
    return producao_total

def main():
    print("--- Registro da Fazenda A ---")
    A = fazendaA()
    
    print("\n--- Registro da Fazenda B ---")
    B = fazendaB()
    
    soma_producao(A, B)

main()
