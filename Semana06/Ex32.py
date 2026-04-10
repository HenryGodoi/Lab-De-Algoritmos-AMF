
cidades = 0
temp_boa = 0

while cidades < 10:
    temperatura = int(input("Digite a temperatura: "))
    
    if temperatura >= 15 and temperatura <= 25:
        temp_boa += 1
    
    cidades += 1

print(f"Foram {temp_boa} cidades que ficaram com a temperatura entre 15 °C e 25 °C")
