 
def ler_lista_inspecao():
    codigos = []
 
    for i in range(5):
        valor = int(input(f"Digite o código do lote {i+1} para inspeção: "))
        codigos.append(valor)
 
    return codigos
 
def verificar_lote(codigos):
    codigo = int(input("\nDigite o código do lote que deseja verificar: "))
    encontrado = False
 
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            encontrado = True
 
    if encontrado:
        print(f"Lote {codigo}: ENCONTRADO na lista de inspeção.")
    else:
        print(f"Lote {codigo}: NÃO ENCONTRADO na lista de inspeção.")
 
def main():
    codigos = ler_lista_inspecao()
    verificar_lote(codigos)
 
main()
