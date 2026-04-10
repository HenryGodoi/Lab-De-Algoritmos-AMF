
jogador = 0
idadevelho = 0
idadenovo = 0
soma_salario = 0
atacante_salario = 0
atacante = 0
defensor = 0

while jogador < 10:
    idade = int(input("Digite a idade: "))
    posicao = input("Digite a posição (A para atacante, D para defensor): ")
    salario = float(input("Digite o salário: "))

    soma_salario += salario
    
    if jogador == 0:
        idadevelho = idade
        idadenovo = idade
    
    if idadevelho < idade:
        idadevelho = idade
    elif idadenovo > idade:
        idadenovo = idade

    if salario <= 10000:
        atacante_salario += 1
    
    if posicao == "A":
        atacante += 1
    elif posicao == "D":
        defensor += 1

    jogador += 1

media_salario = soma_salario / jogador

print(f"A Média dos salários são: {media_salario:.2f}.")
print(f"O jogador mais velho tem {idadevelho} anos e o jogador mais novo tem {idadenovo} anos.")
print("A quantidade de atacantes com salário até $10.000,00 é:", atacante_salario)
print(f"A quantidade de Atacantes é {atacante} e a quantidade de Defensores é {defensor}.")

