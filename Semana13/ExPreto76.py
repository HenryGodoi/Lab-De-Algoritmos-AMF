 
def gerar_ids_lotes():
    ids = []
 
    for i in range(10):
        valor = random.randint(1, 100)
        ids.append(valor)
 
    return ids
 
def exibir_ids_pares(ids):
    pares = []
 
    for i in range(len(ids)):
        if ids[i] % 2 == 0:
            pares.append(ids[i])
 
    print(f"\nTodos os IDs gerados: {ids}")
    print(f"IDs pares (logística): {pares}")
 
    return pares
 
def main():
    print("--- EXERCÍCIO 9: IDs de Lotes e Pares ---")
    ids = gerar_ids_lotes()
    exibir_ids_pares(ids)
 
main()
