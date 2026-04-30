
gasolina = 6.89
diesel = 4.80
opc = 0
opcao = 0
litros_g = 0 
litros_d = 0
valor = 0
litros_total_d = 0
litros_total_g = 0

while opc != 2:
    print()
    print()
    opc = int(input())
    
    if opc == 1:
        print() #1 - gas.
        print() #2 - die.
        opcao = int(input())
    elif opc == 2:
        print()
    else:
        print() #erro
    
    if opcao == 1:
        litros_g = float(input())
        litros_total_g += litros_g
        #valor_pagar = litros * gasolina (Codigo errado)
        valor_pagar = litros_g * gasolina # código reformulado
        print("", valor_pagar)
        valor = float(input())
        troco = valor - valor_pagar
    elif opcao == 2:
        litros_d = float(input())
        #valor_pagar = litros * diesel (Codigo errado)
        valor_pagar = litros_d * diesel # código reformulado
        print("", valor_pagar)
        valor = float(input())
        troco = valor - valor_pagar
        
litros_total = litros_total_g + litros_total_d

porcentos_g = (litros_total_g * 100) / litros_total
porcentos_d = (litros_total_d * 100) / litros_total

print(litros_total_g)
print(litros_total_d)

print(porcentos_g)
print(porcentos_d)
