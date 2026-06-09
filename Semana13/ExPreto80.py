 
def ler_codigos_lote():
    codigos = []
 
    for i in range(5):
        valor = int(input(f"Digite o código do lote {i+1}: "))
        codigos.append(valor)
 
    return codigos
 
def verificar_distintos(codigos):
    tem_duplicata = False
 
    for i in range(len(codigos)):
        for j in range(i + 1, len(codigos)):
            if codigos[i] == codigos[j]:
                tem_duplicata = True
 
    if tem_duplicata:
        print(f"\nCódigos {codigos}: HÁ DUPLICATAS.")
    else:
        print(f"\nCódigos {codigos}: DISTINTOS.")
 
def main():
    print("--- EXERCÍCIO 13: Códigos de Lote Distintos ---")
    codigos = ler_codigos_lote()
    verificar_distintos(codigos)
 
main()
