
pessoas = 0
idade = 0
maioridade = 0

while pessoas < 10:
    idade = int(input("Digite a idade: "))
    
    if idade >= 18:
        maioridade += 1
    
    pessoas += 1
    
print(f"De 10 pessoas que foram entrevistadas, {maioridade} pessoas eram maiores de idade.")
