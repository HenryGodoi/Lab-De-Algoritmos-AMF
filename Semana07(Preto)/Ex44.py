
idade = int(input("Digite a sua idade(0 a 150): "))
while idade < 0 or idade > 150:
    print("Erro! Faça novamente seguindo o que foi pedido.")
    idade = int(input("Digite a idade(0 a 150): "))
    
salario = int(input("Digite o seu salario: "))
while salario <= 0:
    print("Erro! Faça novamente seguindo o que foi pedido.")
    salario = int(input("Digite o seu salario: "))
        
sexo = input("Digite o seu sexo (F ou M): ").upper()
while sexo != "F" and sexo != "M":
    print("Erro! Faça novamente seguindo o que foi pedido.")
    sexo = input("Digite o seu sexo (F ou M): ").upper()

estado_civil = input("Digite o seu Estado Civil (S - Solteiro/a, C - Casado/a, V - Viuvo/a ou D - Divorciado/a): ").upper()
while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print("Erro! Faça novamente seguindo o que foi pedido.")
    estado_civil = input("Digite o seu Estado Civil (S - Solteiro/a, C - Casado/a, V - Viuvo/a ou D - Divorciado/a): ").upper()

print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo.upper()}")
print(f"Estado Civil: {estado_civil.upper()}")
