
clientes = 0
cafe = 0
cappuccino = 0
cha = 0
totalv = 0

while clientes < 10:
    print("---Tabela---")
    print("A - Café Expresso")
    print("B - Cappuccino")
    print("C - Chá")
    opc = input("Escolha a sua bebida favorita: ").upper()
        
    if opc == "A" or "B" or "C":
        totalv += 1
    
    if opc == "A":
        cafe += 1
        print("A sua bebida foi selecionada.")
    elif opc == "B":
        cappuccino += 1
        print("A sua bebida foi selecionada.")
    elif opc == "C":
        cha += 1
        print("A sua bebida foi selecionada.")

    clientes += 1
        
porc_cafe = (cafe / totalv) * 100
porc_capp = (cappuccino / totalv) * 100
porc_cha = (cha / totalv) * 100

print(f"O total de votos para o Café Expresso foram {cafe} votos com preferência de {porc_cafe:.0f}%")
print(f"O total de votos para o Cappuccino foram {cappuccino} votos com preferência de {porc_capp:.0f}%")
print(f"O total de votos para o Chá foram {cha} votos com preferência de {porc_cha:.0f}%")
