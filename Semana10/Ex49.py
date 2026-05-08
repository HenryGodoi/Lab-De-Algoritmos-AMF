
idade = idademaior = 0
individuos_especifico = 0
azuis = 0
verdes = 0
olhos_castanhos = 0
c_loiros = 0
c_castanhos = 0
c_preto = 0
masculino = 0
feminino = 0

for pessoas in range(1, 16):
    sexo = input("Digite o seu sexo: M (masculino) e F (feminino): ").upper()
    olhos = input("Digite a cor dos seus olhos: A (azuis), V (verdes) e C (castanhos): ").upper()
    cabelos = input("Digite a cor do seu cabelo: L (loiros), C (castanhos) e P (pretos): ").upper()
    idade = int(input("Digite a sua idade: "))

    if idademaior < idade:
        idademaior = idade

    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1
    
    if olhos == "A":
        azuis += 1
    elif olhos == "V":
        verdes += 1
    elif olhos == "C":
        olhos_castanhos += 1
    
    if cabelos == "L":
        c_loiros += 1
    elif cabelos == "C":
        c_castanhos += 1
    elif cabelos == "P":
        c_preto += 1
    
    if idade >= 18 and idade <= 35 and olhos == "V" and cabelos == "P":
        individuos_especifico += 1

porcentos_azuis = (azuis * 100) / 15
porcentos_verdes = (verdes * 100) / 15
porcentos_castanhos = (olhos_castanhos * 100) / 15

porcentos_loiros = (c_loiros * 100) / 15
porcentos_cabelo_castanhos = (c_castanhos * 100) / 15
porcentos_c_preto = (c_preto * 100) / 15

porcentos_masculino = (masculino * 100) / 15
porcentos_feminino = (feminino * 100) / 15

print(f"A maior idade é {idademaior} anos.")
print(f"A quantidade de indivíduos cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos pretos é {individuos_especifico} pessoas.")
print(f"A porcentagem de cada olho: Olho Azul: {porcentos_azuis}, Olhos Verdes: {porcentos_verdes}, Olhos Castanhos: {porcentos_castanhos}")
print(f"A porcentagem de cada cabelo: Cabelo Loiro: {porcentos_loiros}, Cabelo Castanho: {porcentos_cabelo_castanhos}, Cabelo Preto: {porcentos_c_preto}")
print(f"A porcentagem dos gêneros: Masculino: {porcentos_masculino}, Feminino: {porcentos_feminino}")
