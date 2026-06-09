 
def codigo_ja_existe(codigos, novo_codigo):
    contador = 0
 
    for i in range(len(codigos)):
        if codigos[i] == novo_codigo:
            contador += 1
 
    return contador
 
def ler_etiquetas_sem_repeticao():
    codigos = []
 
    while len(codigos) < 15:
        codigo = int(input(f"Digite o código da etiqueta {len(codigos) + 1}/15: "))
 
        if codigo_ja_existe(codigos, codigo):
            print(f"Código {codigo} já cadastrado! Informe um código diferente.")
        else:
            codigos.append(codigo)
            print(f"Código {codigo} cadastrado com sucesso.")
 
    return codigos
 
def exibir_etiquetas(codigos):
    print(f"\nEtiquetas cadastradas: {codigos}")
 
def main():
    codigos = ler_etiquetas_sem_repeticao()
    exibir_etiquetas(codigos)
 
main()
