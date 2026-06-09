 
def ler_forcas_equipe():
    forcas = []
 
    for i in range(5):
        valor = int(input(f"Digite a força da equipe no lote {i+1}: "))
        forcas.append(valor)
 
    return forcas
 
def gerar_forcas_pragas():
    forcas = []
 
    while len(forcas) < 5:
        valor = random.randint(1, 100)
 
        if not codigo_ja_existe(forcas, valor):
            forcas.append(valor)
 
    return forcas
 
def simular_confronto(equipe, pragas):
    protegidos = 0
    perdidos = 0
 
    print("\n--- Forças da Equipe vs. Pragas ---")
    print(f"Equipe: {equipe}")
    print(f"Pragas: {pragas}")
 
    print("\n--- Resultado por Lote ---")
    for i in range(len(equipe)):
        if equipe[i] > pragas[i]:
            print(f"Lote {i+1}: Equipe ({equipe[i]}) > Praga ({pragas[i]}) → PROTEGIDO ✔")
            protegidos += 1
        else:
            print(f"Lote {i+1}: Equipe ({equipe[i]}) <= Praga ({pragas[i]}) → PRAGA RESISTIU ✘")
            perdidos += 1
 
    print(f"\n--- Placar Final ---")
    print(f"Lotes protegidos: {protegidos}")
    print(f"Lotes perdidos:   {perdidos}")
 
def main():
    equipe = ler_forcas_equipe()
    pragas = gerar_forcas_pragas()
    simular_confronto(equipe, pragas)
 
main()
