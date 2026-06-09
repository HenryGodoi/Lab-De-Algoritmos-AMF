 
def gerar_ids_controle():
    ids = []
 
    for i in range(10):
        valor = random.randint(1, 50)
        ids.append(valor)
 
    return ids
 
def contar_par_impar(ids):
    pares = 0
    impares = 0
 
    for i in range(len(ids)):
        if ids[i] % 2 == 0:
            pares += 1
        else:
            impares += 1
 
    print(f"\nIDs gerados: {ids}")
    print(f"Quantidade de IDs pares: {pares}")
    print(f"Quantidade de IDs ímpares: {impares}")
 
def main():
    print("--- EXERCÍCIO 11: Par vs. Ímpar no Controle de Lotes ---")
    ids = gerar_ids_controle()
    contar_par_impar(ids)
 
main()
